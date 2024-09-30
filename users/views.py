from rest_framework import viewsets, status, generics
from django.core.mail import send_mail
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import UserRegistrationSerializer, UserLoginSerializer, SendOTPSerializer, VerifyOTPSerializer
from rest_framework.permissions import AllowAny
import requests
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist


class SendOTPView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = SendOTPSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data['phone_number']

        # Check if user exists with that phone number
        try:
            user = CustomUser.objects.get(phone=phone_number)
        except ObjectDoesNotExist:
            return Response({'detail': 'User with this phone number does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        # Generate OTP (you can generate a random OTP here)
        otp_value = '123456'  # Replace with a method to generate a dynamic OTP
        otp_template_name = 'OTP_Template_Name'  # Replace with your actual template name

        # Make a request to 2factor API to send OTP
        url = f'https://2factor.in/API/V1/{settings.TWO_FACTOR_API_KEY}/SMS/{phone_number}/{otp_value}/{otp_template_name}'
        response = requests.get(url)

        if response.status_code == 200:
            # Youmn can store the OTP session ID if needed for verification
            otp_session_id = response.json().get('Details')
            return Response({'message': 'OTP sent successfully', 'otp_session_id': otp_session_id}, status=status.HTTP_200_OK)
        return Response({'detail': 'Failed to send OTP'}, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTPView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = VerifyOTPSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        otp_session_id = serializer.validated_data['otp_session_id']
        otp_entered_by_user = serializer.validated_data['otp_entered_by_user']

        # Make a request to 2factor API to verify OTP
        url = f'https://2factor.in/API/V1/{settings.TWO_FACTOR_API_KEY}/SMS/VERIFY/{otp_session_id}/{otp_entered_by_user}'
        response = requests.get(url)

        if response.status_code == 200 and response.json().get('Details') == 'OTP Matched':
            return Response({'message': 'OTP verified successfully'}, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)



class RegisterView(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer

    # def partial_update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)

    #     if not serializer.is_valid():
    #         # Log the specific errors for debugging
    #         print(f"PATCH request errors: {serializer.errors}")
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #     self.perform_update(serializer)
    #     return Response(serializer.data)


class LoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = authenticate(email=email, password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'email': user.email,
                'user_type': user.user_type,
                'userId': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'date_joined': user.date_joined,
            })
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['POST'])
@permission_classes([AllowAny])
def send_contact_email(request):
    if request.method == 'POST':
        email = request.data.get('email')
        full_name = request.data.get('full_name')
        phone_number = request.data.get('phone_number')
        interest_service = request.data.get('interest_service')
        message_body = request.data.get('message')

        if email:
            subject = 'Contact Form Submission'
            message = f'''
            <html>
            <body>
                <h3>Contact Form Submission</h3>
                <p><strong>Full Name:</strong> {full_name}</p>
                <p><strong>Email Address:</strong> {email}</p>
                <p><strong>Phone Number:</strong> {phone_number}</p>
                <p><strong>Interest Service:</strong> {interest_service}</p>
                <p><strong>Message:</strong> {message_body}</p>
            </body>
            </html>
            '''
            recipient_list = ['info@artstraining.co.uk', 'support@artstraining.co.uk', 'ekenhanson@gmail.com', 'Diana@adada.co.uk']
            from_email = 'admin@artstraining.co.uk'
            send_mail(subject, '', from_email, recipient_list, fail_silently=False, html_message=message)
            return Response({'message': 'Email sent successfully'})
        else:
            return Response({'error': 'Email not provided in POST data'}, status=400)
    else:
        return Response({'error': 'Invalid request method'}, status=400)

