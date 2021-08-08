from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from company.models import Company

class User(AbstractUser):
    USER_TYPE_CHOICES = (
      (1, 'ADMIN'),
      (2, 'USER'),
    )
    email_confirmed = models.BooleanField(default=False)
    avtar  = models.ImageField(upload_to='user_images')
    phone = models.CharField(max_length=20)
    company = models.ForeignKey(Company,related_name="user_company", null=True, on_delete=models.CASCADE)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,default=1)
