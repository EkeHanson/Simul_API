from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobsView

router = DefaultRouter()
router.register(r'jobs', JobsView)

urlpatterns = [
    path('', include(router.urls)),
]
