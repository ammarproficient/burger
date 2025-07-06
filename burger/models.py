from django.db import models


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Burger(models.Model):
    DoesNotExist = None
    objects = None
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='burgers')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='burgers/', blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.full_name}"


class OrderItem(models.Model):
    objects = None
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    burger = models.ForeignKey('Burger', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    item_total = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.burger.name}"

