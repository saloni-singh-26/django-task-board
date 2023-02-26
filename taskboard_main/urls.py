from django.urls import path
from . import  views


urlpatterns = [
    path('task-main', views.product_list, name='task'),
    path('detail/<str:pk>/', views.product_detail, name='task-detail'),
    path('create/', views.product_create, name='task-create'),
    path('update/', views.product_update,name="product-update"),
    path('delete/<str:pk>', views.product_delete, name="product-delete")

]
