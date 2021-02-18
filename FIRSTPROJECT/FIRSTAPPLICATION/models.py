from django.db import models

# Create your models here.
class Candidate(models.Model):
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    Address = models.CharField(max_length=20)
