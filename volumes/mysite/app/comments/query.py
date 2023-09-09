from .models import Comments

def add_comment(content, product_id, user):
	return Comments.objects.create(content=content, product_id=product_id, user=user)
