from rest_framework import viewsets
from .models import UserMessage, Reply
from .serializers import MessageSerializer, ReplySerializer
from rest_framework.permissions import AllowAny
from .pagination import CustomPagination
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework import status


class MessageViewSet(viewsets.ModelViewSet):
    queryset = UserMessage.objects.all().order_by('-id')  # Order by id in descending order
    permission_classes = [AllowAny]
    serializer_class = MessageSerializer
    pagination_class = CustomPagination  # Enable pagination with custom class

    def get_serializer_context(self):
        # Add the request to the context
        context = super().get_serializer_context()
        context.update({
            'request': self.request,
        })
        return context


class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ReplySerializer 

    def create(self, request, *args, **kwargs):
        print("request.data", request.data)
        try:
            response = super().create(request, *args, **kwargs)
            
            if response.status_code == status.HTTP_201_CREATED:
                user = request.data.get('user')
                userEmail = request.data.get('userEmail')
                reply_text = request.data.get('reply_text')

                if userEmail:
                    subject = 'Reply to Message on Simul Website'
                    message = f'''
                    <html>
                    <body>
                        <h3>Contact Form Response</h3>
                        <p><strong>Full Name:</strong> Hi {userEmail}</p>
                        <p><strong>Message:</strong> {reply_text}</p>
                    </body>
                    </html>
                    '''
                    recipient_list = [userEmail]
                    from_email = 'support@artstraining.co.uk'

                    try:
                        send_mail(
                            subject,
                            '',
                            from_email,
                            recipient_list,
                            fail_silently=False,
                            html_message=message
                        )
                        return Response({'message': 'Reply created and email sent successfully'}, status=status.HTTP_201_CREATED)
                    except Exception as e:
                        print(f"Error sending email: {str(e)}")
                        return Response({'error': 'Failed to send email'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                else:
                    return Response({'error': 'Email not provided in POST data'}, status=status.HTTP_400_BAD_REQUEST)

            return response

        except Exception as e:
            print(f"Error during reply creation: {str(e)}")  # Log the error for debugging
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
