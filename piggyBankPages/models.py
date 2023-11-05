from django.db import models

class Transaction(models.Model):
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
