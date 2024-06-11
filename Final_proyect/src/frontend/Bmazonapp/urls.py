from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='bmazon_home'),
    path('', views.login, name='bmazon_login'),
    path('create_account', views.create_account, name = 'bmazon_create_account' ),
    path ('add_product', views.add_product, name = 'bmazon_add_product'),
    path ('electronics ', views.electronics, name = 'bmazon_electronics'),
    path ('fashion', views.fashion, name = 'bmazon_fashion'),
    path ('homekitchen', views.homekitchen , name = 'bmazon_homekitchen'),
    path ('product1', views.product1, name = 'bmazon_product1'),
    path ('shopping_cart', views.shopping_cart, name = 'bmazon_shopping_cart'),
    path ('sportfitness', views.sportfitness, name = 'bmazon_sportfitness')
    
]