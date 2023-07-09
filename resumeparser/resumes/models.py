from django.db import models


class resmesdetails(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mob=models.CharField(max_length=100)
    phone=models.IntegerField(max_length=100)
    gender=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    specilization=models.CharField(max_length=100)
    year=models.IntegerField(max_length=100)
    college=models.CharField(max_length=100)
    resume=models.CharField(max_length=100)