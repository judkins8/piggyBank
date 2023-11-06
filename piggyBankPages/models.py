from django.db import models
from django.conf import settings

class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    
    TRANSACTION_TYPES = (
        ('Allowance', 'Allowance'),
        ('Purchase', 'Purchase'),
    )

    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)

    def save(self, *args, **kwargs):
        if self.transaction_type == 'Purchase':
            self.amount *= -1
        super(Transaction, self).save(*args, **kwargs)

class SavingsGoal(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # If you have additional fields, add them here
