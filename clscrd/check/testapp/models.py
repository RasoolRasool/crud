from django.db import models
from django.urls import reverse

# Create your models here.

class  Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    
    def get_absolute_url(self):
        return reverse('contact_detail',kwargs={'pk':self.pk})