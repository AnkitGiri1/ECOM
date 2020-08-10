from django import forms
from django.shortcuts import render,get_object_or_404
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import address,seller,product

class addproductform(ModelForm):
	class Meta:
		model=product
		fields=['name','price','image','category','delivery_charges']
	def save(self,user1):
		sel=seller.objects.get(user=user1)
		prod=product.objects.create(seller=sel,name=self.fields['name'],price=str(self.fields['price'].value()),category=self.fields['category'],delivery_charges=self.fields['delivery_charges'])
		prod.save()
		return prod

class registerform(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model=User
		fields=["username", "email","first_name","last_name","password1", "password2"]

# class sellerregisterform(UserCreationForm):
# 	email = forms.EmailField()
# 	class Meta:
# 		model=User
# 		fields=["username", "email","first_name","last_name","password1", "password2"]
	
class loginform(forms.Form):
	username=forms.CharField(label="UserName")
	password=forms.CharField(label="Password",widget=forms.PasswordInput)
	username.widget.attrs.update({
	    'class': 'form-control',
	    "name":"username",})
	password.widget.attrs.update({
	    'class': 'form-control',
	    "name":"password",})

class addressform(ModelForm):
	class Meta:
		model = address
		fields = {'add1','add2','city','state','zipcode'}
		widgets = {
            'add1': forms.TextInput(attrs={'class': 'form-control'}),
			'add2': forms.TextInput(attrs={'class': 'form-control'}),
			'city': forms.TextInput(attrs={'class': 'form-control'}),
			'state': forms.TextInput(attrs={'class': 'form-control'}),
			'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
        }
	def is_unique(self,user_id1):
		try:
			add=address.objects.get(add1=self['add1'].value(),add2=self['add2'].value(),city=self['city'].value(),state=self['state'].value(),zipcode=self['zipcode'].value())
			print(add)
			if not add:
				return True
			else:
				return add
		except:
			return True
	