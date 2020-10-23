from django.db import models

class product(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    price=models.CharField(max_length=50)