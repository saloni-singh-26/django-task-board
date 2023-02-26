from django.contrib import admin

from taskboard_main.models import Product, User, Cart_item, Order_detail, Order_item

# Register your models here.

admin.site.register(Product)
admin.site.register(User)
admin.site.register(Cart_item)
admin.site.register(Order_detail)
admin.site.register(Order_item)
