from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cart', views.cart, name='cart'),

    path('signup/', views.reg, name='signup'),  # ← Matches form action
    path('login1/', views.login1, name='login1'),
    path('about/', views.about, name='about'),
    path('logout/', views.logout, name='logout'),

    path('adminpage/', views.adminpage, name='adminpage'),




]



