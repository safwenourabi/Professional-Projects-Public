from django.db import models
from django.contrib.auth.models import User
from django.views.generic import DeleteView
from django.urls import reverse_lazy

# Create your models here.
class ticket(models.Model):
    id= models.AutoField(primary_key=True)
    title = models.CharField()
    description = models.CharField()
    created_date=models.DateField(auto_now_add=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    treated=models.BooleanField()


    

