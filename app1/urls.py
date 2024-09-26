from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('item/create/', views.create_item, name='create_item'),
    path('item/<int:pk>/edit/', views.update_item, name='update_item'),
    path('item/<int:pk>/delete/', views.delete_item, name='delete_item'),
]
