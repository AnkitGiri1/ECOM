from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class seller(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class product(models.Model):
    product_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=64)
    price=models.FloatField()
    image=models.ImageField(upload_to='media/images/')
    category=models.CharField(max_length=16,default="no")
    delivery_charges=models.FloatField(null=True)
    seller=models.ForeignKey(seller,on_delete=models.CASCADE)

class cart(models.Model):
    product_id=models.ForeignKey(product,on_delete=models.CASCADE)
    user_id=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)

class address(models.Model):
    add1=models.CharField(max_length=60)
    add2=models.CharField(max_length=60)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zipcode=models.CharField(max_length=20)
    def __str__(self):
        return "add1:{},add2:{},city:{},state:{},zipcode:{}".format(self.add1,self.add2,self.city,self.state,self.zipcode)

class order(models.Model):
    order_id=models.AutoField(primary_key=True)
    address=models.ForeignKey(address,on_delete=models.CASCADE)
    user_id=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    date=models.DateField(null=True)
    delivery=models.FloatField(null=True)
    total=models.FloatField(null=True)


class order_items(models.Model):
    order_id=models.ForeignKey(order,on_delete=models.CASCADE)
    product_id=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)