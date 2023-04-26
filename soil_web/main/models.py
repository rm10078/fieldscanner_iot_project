from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .modelManager import CustomUserManager


class MyUser(AbstractBaseUser):         
                                            
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    address=models.CharField(max_length=500)
    mobileNumber=models.CharField(max_length=13)
    fieldArea=models.DecimalField(max_digits=5,decimal_places=2,default=00.00)
    plantName=models.CharField(max_length=50)
    deviceID=models.CharField(max_length=50,unique=True)
                                        
    USERNAME_FIELD = 'email'            
    REQUIRED_FIELDS = ['first_name', 'last_name']  
    
    objects = CustomUserManager()
                                  
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

# Create your models here.

class deviceData(models.Model):
    deviceId=models.CharField(max_length=255)
    soilN=models.DecimalField(max_digits=5,decimal_places=2)
    soilP=models.DecimalField(max_digits=5,decimal_places=2)
    soilK=models.DecimalField(max_digits=5,decimal_places=2)
    soilMos=models.DecimalField(max_digits=5,decimal_places=2)
    light=models.DecimalField(max_digits=7,decimal_places=2)
    lightR=models.DecimalField(max_digits=7,decimal_places=2)
    lightG=models.DecimalField(max_digits=7,decimal_places=2)
    lightB=models.DecimalField(max_digits=7,decimal_places=2)
    tem=models.DecimalField(max_digits=5,decimal_places=2)
    hum=models.DecimalField(max_digits=5,decimal_places=2)
    bstatus=models.DecimalField(max_digits=5,decimal_places=2)
    utime=models.DateTimeField()

    def __str__(self):
        return self.deviceId
