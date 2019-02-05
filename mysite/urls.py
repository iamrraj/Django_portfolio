from django.urls import path

from . import views

from .views import (BlogDetailView)

urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('rahul/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    # path('portfolio', views.portfolio, name='portfolio'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('rahul/new/product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),

]
