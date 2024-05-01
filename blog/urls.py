from collections import UserList

from django.urls import path
from .views import *

urlpatterns = [
    path('order/', OrderList.as_view(), name='order-list'),
    path('order/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    path('book/', BookList.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('profile/', ProfileList.as_view(), name='profile-list'),
    path('category/', CategoryList.as_view(), name='category-list'),
    path('about/', AboutList.as_view(), name='about-list'),
]