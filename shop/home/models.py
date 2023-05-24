from django.db import models

# Create your models here.
class Data(models.Model):
    name=models.CharField(("name"), max_length=50)
    pno=models.CharField(("pno"), max_length=50)
    email=models.CharField(("email"), max_length=50)
    address=models.CharField(("address"), max_length=50)
    dob=models.CharField(("dob"), max_length=50)
    bg=models.CharField((""), max_length=50)
class Credentials(models.Model):
    username=models.CharField(("Username"), max_length=50)
    Password=models.CharField(("Password"), max_length=50)