from django.db import models

# Create your models here.


class Staff(models.Model):
    fullname = models.CharField(max_length=100)
    staff_id = models.CharField(max_length=4)
    contact_no = models.CharField(max_length=15)
    address = models.CharField(max_length=50)