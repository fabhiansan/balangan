from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('databor', views.AllBorView)
router.register('reklamasi', views.WwmReklamasiView)

urlpatterns = [
    path('', include(router.urls))
]
