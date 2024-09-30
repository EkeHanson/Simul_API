from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, ReplyViewSet

router = DefaultRouter()
router.register(r'messages', MessageViewSet)
router.register(r'replies', ReplyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
