from django.db import models

# Create your models here.

class VendoRegistration(models.Model):
    PI_CHOICES = [
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    pi_model = models.IntegerField(default=0)
    serial_number = models.CharField(max_length = 16, default='')
    bch_wallet_address = models.CharField(max_length = 50, default='')
    bch_vendo_name = models.CharField(max_length = 50, default='')
    product_items_available = models.IntegerField(default=0)

    def __str__(self):
        return self.bch_vendo_name

    class Meta:
        verbose_name_plural = 'Vendo Registration'

#Products Table
class ProductItem(models.Model):
    bch_vendo = models.ForeignKey(VendoRegistration, on_delete=models.CASCADE, default=1)
    PRODUCT_CODES = [
        ('A01', 'A01'),
        ('A02', 'A02'),
        ('A03', 'A03'),
        ('A04', 'A04'),
        ('B05', 'B05'),
        ('B06', 'B06'),
        ('B07', 'B07'),
        ('B08', 'B08'),
        ('C09', 'C09'),
        ('C10', 'C10'),
        ('C11', 'C11'),
        ('C12', 'C12'),
        ('D13', 'D13'),
        ('D14', 'D14'),
        ('D15', 'D15'),
        ('D16', 'D16'),
    ]
    product_code = models.CharField(max_length = 3, choices= PRODUCT_CODES)
    product_name = models.CharField(max_length = 50, default='')
    product_quantity = models.IntegerField(default=0)   
    product_price = models.DecimalField(max_digits = 10, decimal_places=2)
    product_image = models.ImageField(upload_to='products')
    
    

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = 'Product Items'
