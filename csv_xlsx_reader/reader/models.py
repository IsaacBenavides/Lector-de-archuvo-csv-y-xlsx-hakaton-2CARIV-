from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Uploader(models.Model):

    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="media/files")
    upload_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.name


class Xlsx(models.Model):
    region = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    item_type = models.CharField(max_length=255)
    sales_channel = models.CharField(max_length=255)
    order_priority = models.CharField(max_length=255)
    order_date = models.DateField()
    order_id = models.IntegerField()
    ship_date = models.DateField()
    units_sold = models.IntegerField()
    unit_price = models.FloatField()
    unit_cost = models.FloatField()
    total_revenue = models.FloatField()
    total_cost = models.FloatField()
    total_profit = models.FloatField()
    document = models.ForeignKey(Uploader, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_type + ' ' + self.sales_channel + ' ' + self.order_date


class CsvModel(models.Model):
    date = models.DateField()
    description = models.TextField()
    deposits = models.DecimalField(decimal_places=2, max_digits=30)
    withdrawls = models.DecimalField(decimal_places=2, max_digits=30)
    balance = models.DecimalField(decimal_places=2, max_digits=30)
    document = models.ForeignKey(Uploader, on_delete=models.CASCADE)
