from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from backend import views

router = DefaultRouter()
router.register(r'backend', views.CountryViewSet)
router.register(r'backend/(?P<code>\w+)/states', views.StateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]