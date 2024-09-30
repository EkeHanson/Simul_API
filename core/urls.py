from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenVerifyView,TokenRefreshView,)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/accounts/', include('users.urls')),
    path('api/news/update/', include('news.urls')),
    path('api/messages/update/', include('user_message.urls')),

    path('api/client-tracking/', include('client_tracking.urls')),  # IP tracking and GDPR consent
    path('api/bookings/', include('bookings.urls')),  # Consultations/Bookings
    
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
