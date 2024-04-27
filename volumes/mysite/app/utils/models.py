from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self) -> str:
        return self.name
    
class BugBounty(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.title