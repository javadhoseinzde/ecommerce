from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import update_session_auth_hash
from rest_framework import status
from ..models import MyUser
from ..helper import get_random_otp

class UserViewSet(APIView):
    def post(self, request):
        mobile = request.data.get('mobile')
        try:
            user = MyUser.objects.get(mobile=mobile)
        except MyUser.DoesNotExist:
            return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        otp = get_random_otp()
        # user.password = otp
        user.set_password(str(otp))
        user.save()
        update_session_auth_hash(request, user)

        print(otp)

        return Response({'message': 'OTP has been sent to your email.'}, status=status.HTTP_200_OK)