from django.urls import path
from .views import DeviceRegistrationView, GasNotificationView




urlpatterns = [
	path('register-device/', DeviceRegistrationView.as_view(), name='register_device'),
	path('send-notification/', GasNotificationView.as_view(), name='send-notification'),
]