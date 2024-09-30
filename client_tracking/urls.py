from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientIPViewSet, GDPRConsentViewSet

router = DefaultRouter()
router.register(r'ips', ClientIPViewSet, basename='clientip')
router.register(r'gdpr-consents', GDPRConsentViewSet, basename='gdprconsent')

urlpatterns = [
    path('', include(router.urls)),
]
