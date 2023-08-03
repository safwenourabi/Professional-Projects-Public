from django.db import models

# Create your models here.
class accounts(models.Model):
    id= models.AutoField(primary_key=True)
    username = models.CharField()
    password = models.CharField()
    created_date=models.DateField(auto_now_add=True)
    level=models.IntegerField(max_length=2, default=1)

