from django.db import models
from django.contrib.auth.models import User
import os
import random

def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext

def upload_image_path(instance, filename):
	new_filename = random.randint(1, 2541781232)
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
	return "img/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)
    
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    download = models.FileField(null=True, blank=True)
    watch = models.CharField(max_length=200, null=True, blank=True)
    isBasic = models.BooleanField(default=False)
    isPremium = models.BooleanField(default=False)
    preorderdate = models.DateField(auto_now_add=False, null=True, blank=True)
    numofPreorder = models.IntegerField(null=True, blank=True, default=0)
    isBought = models.BooleanField(default=True)

    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name



    
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)   
    name = models.CharField(max_length=200, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.rating)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)
    taxPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    shippingPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    totalPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    download = models.FileField(null=True, blank=True)
    isBasic = models.BooleanField(default=False)
    isPremium = models.BooleanField(default=False)
    preorderdate = models.DateField(auto_now_add=False, null=True, blank=True)
    isBought = models.BooleanField(default=False)

    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.createdAt)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    isBasic = models.BooleanField(default=False)
    isPremium = models.BooleanField(default=False)
    download = models.CharField(max_length=200, null=True, blank=True)
    preorderdate = models.DateField(auto_now_add=False, null=True, blank=True)
    isBought = models.BooleanField(default=True)

    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class ShippingAddress(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.address)


class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_of_friend = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False, default=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
   

    
class Song(models.Model):
    music = models.FileField(null=True, blank=True)
    music2 = models.FileField(null=True, blank=True)
    music3 = models.FileField(null=True, blank=True)
    music4 = models.FileField(null=True, blank=True)
    music5 = models.FileField(null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    title2 = models.CharField(max_length=200, null=True, blank=True)
    title3 = models.CharField(max_length=200, null=True, blank=True)
    title4 = models.CharField(max_length=200, null=True, blank=True)
    title5 = models.CharField(max_length=200, null=True, blank=True)

    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

   
   
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.CharField(max_length=200, null=True, blank=True)
    download = models.FileField(null=True, blank=True)
    watch = models.CharField(max_length=200, null=True, blank=True)

    preorderdate = models.DateField(auto_now_add=False, null=True, blank=True)
    numofPreorder = models.IntegerField(null=True, blank=True, default=0)

    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name
    
class Review(models.Model):
    song = models.ForeignKey(Song, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.rating)
    
class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='playlists/', blank=True, null=True)
    link = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

