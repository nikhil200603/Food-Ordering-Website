from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Student(models.Model):
    # id=models.AutoField() # this is automatically added by Django
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)



class car(models.Model):
    car_name=models.CharField(max_length=500)
    speed=models.IntegerField(default=50)

    def __str__(self):
        return self.car_name+" "+str(self.speed)

@receiver(post_save,sender = car)
def car_api(sender,instance,**kwargs):
    print("CAR OBJECT CREATED")
    print(sender,instance,kwargs)




class Product(models.Model):
    pass
# Create your models here.
