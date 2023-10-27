from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# piggybank_app/models.py


class Child(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields specific to a child

class AllowanceEntry(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    chore_description = models.CharField(max_length=255)

class Purchase(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
