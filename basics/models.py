from django.db import models

# Create your models here.




class Order(models.Model):

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    product_type = models.CharField(max_length=50)

    frame = models.CharField(max_length=50, null=True, blank=True)
    size = models.CharField(max_length=50, null=True, blank=True)

    keychain = models.CharField(max_length=50, null=True, blank=True)

    message = models.TextField(null=True, blank=True)

    note = models.TextField(null=True, blank=True)

    photo1 = models.ImageField(upload_to="orders/", null=True, blank=True)
    photo2 = models.ImageField(upload_to="orders/", null=True, blank=True)

    def __str__(self):
        return self.name

class Register(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name