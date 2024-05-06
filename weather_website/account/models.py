from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Account(models.Model):
    # Makes one user per account
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Model for our Accounts
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    notifications = models.BooleanField(default=False)
    
    # Designates layout for phone number
    phone_regex = RegexValidator(regex=r'^\+\d{8,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=16, blank=True) # Validators should be a list
    
    def __str__(self):
        return self.first_name   
