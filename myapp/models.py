from django.db import models

# Create your models here.
import email
from django.db import models

class Donor(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    # aadhar_card = models.CharField(max_length=50)
    # pan_card = models.CharField(max_length=50)
    upline_id = models.CharField(max_length=50)
    def __str__(self):
        return self.name