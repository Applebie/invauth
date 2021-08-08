from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


class Company(models.Model):
    TEMPLATE_CHOICES=(
        (0,'default'),
         (1,'select1')
    )
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    company_website = models.CharField(max_length=70)  
    fax_number = models.CharField(max_length=70)

    street = models.TextField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50) 
    country = models.CharField(max_length=50)
    logo  = models.ImageField(upload_to='company_images')
    template  = models.PositiveSmallIntegerField(choices=TEMPLATE_CHOICES, default=0)
    stripe_id = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ('-pk',)
        db_table = "company"

    def __str__(self):
        return '{}'.format(self.name) 
    

# Our API endpoints will include the following:

# api/company: this endpoint is used to create students and return a list of company.
# api/company/<pk:id>: this endpoint is used to get, update, and delete single company by id or primary key.