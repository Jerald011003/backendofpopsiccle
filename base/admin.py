from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
# admin.site.register(Friend)
# admin.site.register(Chat)
admin.site.register(Song)
admin.site.register(Playlist)

