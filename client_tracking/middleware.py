# client_tracking/middleware.py
from .models import ClientIP

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class ClientIPTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = get_client_ip(request)

        # Check if the IP address already exists
        existing_ip = ClientIP.objects.filter(ip_address=ip).first()
        if not existing_ip:
            ClientIP.objects.create(ip_address=ip)

        response = self.get_response(request)
        return response
