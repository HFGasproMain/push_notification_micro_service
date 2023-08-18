from rest_framework import views, status
from rest_framework.response import Response
from firebase_admin.messaging import Message
from fcm_django.models import FCMDevice

# Create your views here.
class DeviceRegistrationView(views.APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        device_token = request.data.get('device_token')

        if not user_id or not device_token:
            return Response({'error': 'Missing user ID or device token'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the device is already registered
        existing_device = FCMDevice.objects.filter(registration_id=device_token).first()

        if existing_device:
            return Response({'message': 'Device already registered'}, status=status.HTTP_200_OK)

        # Register the device for the user
        new_device = FCMDevice(registration_id=device_token, user_id=user_id)
        new_device.save()

        return Response({'message': 'Device registered successfully'}, status=status.HTTP_201_CREATED)



class GasNotificationView(views.APIView):
    def post(self, request):
        gas_usage = request.data.get('gas_usage')
        gas_remaining = request.data.get('gas_remaining')
        user_id = request.data.get('user_id')
        user_name = request.data.get('user_name')  
        gas_reading = request.data.get('gas_reading')  
        custom_message = request.data.get('custom_message')  # Customized message
        

        try:
            device = FCMDevice.objects.get(user_id=user_id)
            device_token = device.registration_id
            #device_token = str(device_token)

            print("device deets: ", device, " and the device_token is: ", device_token)
        except FCMDevice.DoesNotExist:
            return Response({'error': 'Device not found'}, status=status.HTTP_404_NOT_FOUND)

        # Customize the message based on your requirements
        if custom_message:
            message = custom_message
        else:
            message = f'Hello {user_name}, your gas usage is {gas_usage} and remaining is {gas_remaining}. \
            Your latest gas reading is {gas_reading}. Love from Homefort'

         # Create a Message object
        message = Message(data={
            'gas_usage': gas_usage,
            'gas_remaining': gas_remaining,
        })

        # Set the token attribute of the Message object
        message.token = device_token

        # Send the notification to the device
        device.send_message(message)

        # device.send_message(title='Gas Notification', message=message, data={
        #     "token": device_token,
        #     'gas_usage': gas_usage,
        #     'gas_remaining': gas_remaining,
        # })

        return Response({'success': 'Notification sent'}, status=status.HTTP_200_OK)
