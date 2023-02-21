from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class payments(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    paid_unpaid=models.BooleanField(default=False)
    # text=models.CharField(max_length=10)
    
    
class payment(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    paid_unpaid=models.BooleanField(default=False)
    text=models.CharField(max_length=10)
        