from kavenegar import *
from config.settings.kavenegar import Kavenegar_API
from random import randint
from . import models
import datetime
def send_otp(mobile, otp):
    print(mobile)
    try:
        api = KavenegarAPI(Kavenegar_API)
        params = {
            'sender': '2000500666',#optional
            'receptor': mobile, #multiple mobile number, split by comma
            'message': 'سلام تضمینی کالا',
        } 
        response = api.sms_send(params)
        print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)
    print("OTP", otp)

def get_random_otp():
    return randint(1000, 9999)

def check_otp_expiration(mobile):
    try:
        user = models.MyUser.objects.get(mobile=mobile)
        now = datetime.datetime.now()

        print(now)
        otp_time = user.otp_create_time
        print(type(otp_time))
        print(otp_time)
        diff_time =now - otp_time
        print("OTP dif time",diff_time)
        if diff_time.seconds > 30:
            return False
        else:
            return True
    except models.MyUser.DoesNotExist:
        return False