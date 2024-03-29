from django.db import models
from django.contrib.auth.models import User

class Questions(models.Model):
    title=models.TextField(null=True, blank=True)
    status=models.CharField(default='Inactive', max_length=10)
    created_by=models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    start_date=models.DateTimeField(null=True,blank=True)
    end_date=models.DateTimeField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Choice(models.Model):
    text=models.TextField(null=True,blank=True)
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
