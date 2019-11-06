from django.db import models

# Create your models here.
class Doctor(models.Model):    
    name=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    experience=models.IntegerField()
    fee=models.IntegerField()
    available=models.CharField(max_length=200)
    booked=models.DecimalField(max_digits=5,decimal_places=0, default=0)
    
    def __str__(self):
        return self.name 