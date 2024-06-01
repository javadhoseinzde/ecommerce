import requests
import json
from app.order.models import Order
merchant = "8e25464f-3cc2-4f5a-a21d-e6e7e90ecefc"

def send_request(amount, description, id):
    data = {
        "merchant_id": merchant,
        "amount": amount,
        "description": description,
#        "phone": phone,
        "callback_url": f"http://techykala.com/verify/payment/{id}/{amount}",
    }
    ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
    data = json.dumps(data)
    headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
    try:
        response = requests.post(ZP_API_REQUEST, data=data,headers=headers, timeout=10)
        return response.json()
    except requests.exceptions.Timeout:
        print("except")


#print(send_request())




def verify(amount, authority, Status, id):
    print("verify")
    print(authority)
    print("verify")
    data = {
        "merchant_id": merchant,
        "amount": amount,
        "authority": authority,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json'}
    ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
    response = requests.post(ZP_API_VERIFY, data=data,headers=headers)
    print(response.text)
    if response.status_code == 200:
        response = response.json()
        print("status_code == 200")
        try:
            if Status == "OK":
                query = Order.objects.filter(id=id).update(paid="True")
                return {'status': True, 'RefID': response['ref_id']}
        except:
                print("else")
                return {'status': False, 'code': str(Status)}
    return response
