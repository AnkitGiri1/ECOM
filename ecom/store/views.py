from django.shortcuts import render,get_object_or_404
from .forms import registerform,loginform,addressform,addproductform
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import product,cart,address,order,order_items,seller
from django import forms
import datetime

def addproduct(request):
	if request.method=='POST':
		form=addproductform(request.POST,request.FILES)
		if form.is_valid():
			form.save(request)
			return HttpResponseRedirect('/seller_dashboard')
		else:
			is_seller=seller.objects.filter(user=request.user)
			context={'form':form,'seller':is_seller}
			return render(request,'store/addproduct.html',context)
	form=addproductform()
	is_seller=seller.objects.filter(user=request.user)
	context={'form':form,'seller':is_seller}
	return render(request,'store/addproduct.html',context)

def sellerdashboard(request):
	is_seller=seller.objects.filter(user=request.user)
	products=product.objects.filter(seller=is_seller[0])
	orders=order_items.objects.filter(product_id__seller=is_seller[0])
	context={'products':products,'orders':orders,'seller':is_seller}

	return render(request,'store/seller_dashboard.html',context)
def userlogin(request):
	if request.method == 'POST':
		form=loginform(request.POST)
		if form.is_valid():
			user=authenticate(request=request,username=request.POST['username'],password=request.POST['password'])
			if user is not None:
				login(request,user)
				return HttpResponseRedirect("/product")
	else:
		form=loginform()
	context={ 'form':form }
	return render(request,'store/login.html',context)

def userlogout(request):
	logout(request)
	return HttpResponseRedirect('/login/')

def usersignup(request):
	if request.method == 'POST':
		form=registerform(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('/thanks/')
	else:
		form=registerform()
	context={ 'form': form }
	return render(request,'store/signup.html',context)

def index(request):
	is_seller=seller.objects.filter(user=request.user)
	context={'seller':is_seller}
	return render(request,'store/index.html',context)

def productview(request):
	products=product.objects.all()
	if request.user.is_authenticated:	
		carts=list(cart.objects.filter(user_id=request.user))
		carts_l=map((lambda cart1: cart1.product_id.product_id),carts)
		carts_l=list(carts_l)
		for product1 in products:
			product1.incart=product1.product_id in carts_l
		is_seller=seller.objects.filter(user=request.user)
	context={'products':products,'seller':is_seller}
	return render(request,'store/product.html',context)

@login_required(login_url='/login/') 
def cartview(request):
	# try:
	# 	add=get_object_or_404(address,user_id=request.user)
    # except MyModel.DoesNotExist:
    #     raise Http404("No MyModel matches the given query.")
	# form=addressform(instance=add)
	form=addressform()
	carts=cart.objects.filter(user_id=request.user)
	total=0
	tax=0
	shipping=60
	for cart1 in carts:
		total+=cart1.product_id.price*cart1.quantity
	g_total=total+shipping+tax
	bill={'total':total,'tax':tax,'shipping':shipping,'gtotal':g_total}
	is_seller=seller.objects.filter(user=request.user)
	context={'carts':carts,'bill':bill,'form':form,'seller':is_seller}
	return render(request,'store/cart.html',context)

@login_required(login_url='/login/')
def addtocart(request):
	prod_id=request.GET['product_id']
	prod=get_object_or_404(product,product_id=prod_id)
	cart1=cart.objects.filter(product_id=prod,user_id=request.user)
	rem=request.GET.get('min', False)
	if rem==False:
		if not cart1:
			cart1=cart(product_id=prod,user_id=request.user,quantity=1)
			cart1.save()
		else:
			for cart2 in cart1:
				cart2.quantity+=1
				cart2.save()
	else:
		if rem=='1':
			for cart2 in cart1:
				if cart2.quantity>1:
					cart2.quantity-=1
					cart2.save()
				else:
					cart2.delete()
		elif rem=='all':
			for cart2 in cart1:
				cart2.delete()
	# context={'carts':cart1}
	# return render(request,'store/cart.html',context)
	return HttpResponseRedirect(request.GET.get('next','/cart'))

@login_required(login_url='/login/')
def ordersview(request):
	form=addressform(request.POST)
	# print(form.is_valid())
	orderplaced=False
	if form.is_valid():
		if form.is_unique(request.user)==True:
			add=form.save()
		else:
			add=form.is_unique(request.user)
	else:
		# form=addressform()
		orders=order.objects.filter(user_id=request.user)
		for order1 in orders:
			order1.items=order_items.objects.filter(order_id=order1)
		is_seller=seller.objects.filter(user=request.user)
		context={'orders':orders,'orderplaced':orderplaced,'seller':is_seller}
		return render(request,'store/checkout.html',context)
	orderplaced=True
	carts=cart.objects.filter(user_id=request.user)
	d=0
	t=0
	for cart1 in carts:
		t+=cart1.product_id.price*cart1.quantity
		d=max(d,cart1.product_id.delivery_charges)
	t+=d
	order_obj=order.objects.create(user_id=request.user,address=add,date= str(datetime.date.today()),delivery=d,total=t)
	for cart1 in carts:
		order1=order_items.objects.create(product_id=cart1.product_id,quantity=cart1.quantity,order_id=order_obj)
		cart1.delete()
	orders=[order_obj]
	# orders=order.objects.filter(user_id=request.user)
	for order1 in orders:
		order1.items=order_items.objects.filter(order_id=order1)
	is_seller=seller.objects.filter(user=request.user)
	context={'orders':orders,'orderplaced':orderplaced,'seller':is_seller}
	return render(request,'store/checkout.html',context)

def sellersignup(request):
	if request.method == 'POST':
		form=registerform(request.POST)
		if form.is_valid():
			us=form.save()
			seller.objects.create(user=us)
			return HttpResponse('/thanks/')
	else:
		form=registerform()
	context={ 'form': form }
	return render(request,'store/sellersignup.html',context)
