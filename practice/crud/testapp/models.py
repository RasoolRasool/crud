from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
    bio=models.DateField(null=True,blank=True)
    location=models.CharField(max_length=30,blank=True)
    
    def save(self):
        super().save()

    
class Question(models.Model):
    title=models.CharField(max_length=40,null=True,blank=False)
    status=models.CharField(default='inactive',max_length=30)
    created_by=models.ForeignKey(User,null=True,blank=False,on_delete=models.CASCADE)
    start_date=models.DateTimeField(null=True,blank=False)
    end_date=models.DateTimeField(null=True,blank=False)
    created_at=models.DateTimeField(null=True,blank=False)
    updated_at=models.DateTimeField(null=True,blank=False)

    def __str__(self):
        return self.title