from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.

class Group(models.Model):
    name=models.CharField(max_length=50, null=True, blank=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now())
    members= models.ManyToManyField(User,related_name='members',null=True,blank=True)
    created_at=models.DateTimeField(default=datetime.now())
    

    def __str__(self):
        return str(self.name)