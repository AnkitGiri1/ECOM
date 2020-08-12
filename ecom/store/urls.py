from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.productview, name="index"),
	path('login/', views.userlogin, name="login"),
	path('signup/', views.usersignup, name="signup"),
	path('logout/',views.userlogout,name='logout'),
	path('product/',views.productview,name='product'),
	path('cart/',views.cartview,name='cart'),
	path('cart/add/',views.addtocart,name='addtocart'),
	path('orders/',views.ordersview,name='orders'),
	path('sellersignup',views.sellersignup,name='sellersignup'),
	path('seller_dashboard',views.sellerdashboard,name='seller_dashboard'),
	path('addproduct',views.addproduct,name='addproduct')
		
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
