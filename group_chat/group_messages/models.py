from django.db import models
from datetime import datetime
from group.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Message(models.Model):
    description=models.CharField(max_length=100, null=False, blank=False)
    messaged_by=models.ForeignKey(User,on_delete=models.CASCADE)
    messaged_at = models.DateTimeField(default=datetime.now())
    is_liked=models.BooleanField(default=False)
    liked_by=models.ForeignKey(User,related_name='liked_by',on_delete=models.CASCADE,null=True,blank=True)
    group=models.ForeignKey(Group,related_name='messages',on_delete=models.CASCADE)

    def __str__(self):
        return self.description
