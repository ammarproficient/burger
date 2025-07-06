from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # default home page
    path('burger/<int:pk>/', views.burger_detail, name='burger_detail'),
    path('category/<int:category_id>/', views.home, name='burger_by_category'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('cart/increase/<int:pk>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:pk>/', views.decrease_quantity, name='decrease_quantity'),
    path('checkout/', views.checkout_view, name='checkout'),

]
