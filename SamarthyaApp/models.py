from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class bool_model(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    true_false=models.BooleanField(default=False)

    def __str__(self):
        return str(self.true_false)

