from django.urls import path
from . import views

urlpatterns = [
    path('products', views.getProducts),
    path('add-product', views.addItem),
    path('delete-product/<int:pk>', views.deleteItem),
    path('update-product/<int:pk>', views.updateItem),
]