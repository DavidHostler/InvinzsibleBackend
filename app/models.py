from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.CharField(primary_key=True,max_length=15)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150,default="NA")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.id
    
    class Meta:
        db_table = "product_details"
#Auschwitz41

class Order(models.Model):
    order_id = models.CharField(primary_key=True,max_length=15)
    address = models.CharField(max_length=50)
    customer_id = models.CharField(max_length=15)
    payment = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    
    def __str__(self):
        return self.order_id




    class Meta:
        db_table = "order_details"


class Cart(models.Model):
    cart_id = models.CharField(primary_key=True,max_length=15)
    cart_name = models.CharField(max_length=50)
    cart_description = models.CharField(max_length=150,default="NA")
    cart_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    cart_category = models.CharField(max_length=50)

    def __str__(self):
        return self.cart_id
    
    class Meta:
        db_table = "cart_details"