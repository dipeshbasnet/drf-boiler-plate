from django.urls import path
from rest_framework import routers

from .views.demo import DemoView, DemoViewSet

ROUTER = routers.DefaultRouter()

ROUTER.register('demo', DemoViewSet, basename='demo-viewset')

urlpatterns = ROUTER.urls
