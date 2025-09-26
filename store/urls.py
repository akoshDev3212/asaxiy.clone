from django.urls import path
from . import views

urlpatterns = [
   path('' , views.store, name='store' ),
   path('<slug>/detail', views.products_detail, name='products_detail'),
]
