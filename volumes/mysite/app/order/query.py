from .models import Order

def create_order(first_name, last_name, email, address, postal_code, city, user):
    
    return Order.objects.create(first_name=first_name, last_name=last_name,
                                 email=email, address=address,postal_code=postal_code, city=city, user=user)