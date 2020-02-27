from .views import *
from rest_framework.routers import DefaultRouter
from django.conf.urls import url

router = DefaultRouter()
router.register(r'^property', PropertyView, base_name='property')
router.register(r'^booking', BookingView, base_name='booking')


urlpatterns = [
]
urlpatterns += router.urls