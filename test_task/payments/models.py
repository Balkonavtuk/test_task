from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Payment(models.Model):
    payer = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    percent = models.IntegerField()  # или DecimalField, если нужна точность
    pay_date = models.DateTimeField()

    def __str__(self):
        return f"Payment {self.id} by {self.payer}"
