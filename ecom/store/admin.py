from django.contrib import admin
from .models import product,cart,address,order,order_items,seller

class productadmin(admin.ModelAdmin):
    list_display = ('name', 'price','category','view_seller')
    def view_seller(self, obj):
        return obj.seller.user


class cartadmin(admin.ModelAdmin):
    list_display = ('user_id', 'product_id','quantity')
    

admin.site.register(cart,cartadmin)
admin.site.register(product,productadmin)
admin.site.register(address)
admin.site.register(order)
admin.site.register(order_items)

admin.site.register(seller)

