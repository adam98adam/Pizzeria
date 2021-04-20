from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255, blank=False)
    surname = models.CharField(max_length=255, blank=False)
    email = models.CharField(max_length=255, blank=False, unique=True)
    phonenumber = models.CharField(max_length=255, blank=False, unique=True)
    customer = models.BooleanField(default=True)


class Customeraddress(models.Model):
    city = models.CharField(max_length=255, blank=False)
    street = models.CharField(max_length=255, blank=False)
    number = models.IntegerField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Account(models.Model):
    login = models.CharField(max_length=255, blank=False, unique=True)
    password = models.CharField(max_length=255, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Bakestyle(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)


class Crust(models.Model):
    crust = models.CharField(max_length=255, blank=False, unique=True)
    price = models.FloatField(blank=False)


class Cutstyle(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)


class Pizzasize(models.Model):
    diameter = models.IntegerField(blank=False, unique=True)
    ingredientcostfactor = models.FloatField(blank=False,unique=True)
    name = models.CharField(max_length=255, blank=False, unique=True)
    price = models.FloatField(blank=False, unique=True)


class Pizzaside(models.Model):
    name = models.CharField(max_length=255, blank=False)


class Ingredienttype(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)


class Ingredient(models.Model):
    imagefilename = models.CharField(max_length=255, blank=False, unique=True)
    name = models.CharField(max_length=255, blank=False, unique=True)
    price = models.FloatField(blank=False)
    ingredienttype = models.ForeignKey(Ingredienttype, on_delete=models.CASCADE)


class Pizzaitem(models.Model):
    quantity = models.IntegerField(blank=False)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    pizzaside = models.ManyToManyField(Pizzaside)


class Pizza(models.Model):
    bakestyle = models.ForeignKey(Bakestyle, on_delete=models.CASCADE)
    crust = models.ForeignKey(Crust, on_delete=models.CASCADE)
    cutstyle = models.ForeignKey(Cutstyle, on_delete=models.CASCADE)
    left_pizzaside = models.ForeignKey(Pizzaside, related_name='left_pizzaside', on_delete=models.CASCADE)
    right_pizzaside = models.ForeignKey(Pizzaside, related_name='right_pizzaside', on_delete=models.CASCADE)
    size = models.ForeignKey(Pizzasize, on_delete=models.CASCADE)


class Order(models.Model):
    comment = models.CharField(max_length=255)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)


class Deliveryaddress(models.Model):
    city = models.CharField(max_length=255, blank=False)
    street = models.CharField(max_length=255, blank=False)
    number = models.IntegerField(blank=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class Orderitem(models.Model):
    quantity = models.IntegerField(blank=False)
    order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)


class Orderitemtemplate(models.Model):
    description = models.CharField(max_length=255)
    imagefilename = models.CharField(max_length=255, blank=False, unique=True)
    orderitem = models.ForeignKey(Orderitem, on_delete=models.CASCADE)
