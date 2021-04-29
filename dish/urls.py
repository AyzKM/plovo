from django.urls import path
from dish.views import *

urlpatterns = [
    path('', DishListAPIView.as_view(), name='dishes'),
    path('create/', DishCreateAPIView.as_view(), name='dish-create'),
    path('<int:pk>/', DishDetailAPIView.as_view(), name='dish'),
    path('<int:pk>/delete/', DishDeleteAPIView.as_view(), name='dish-delete'),
    path('<int:pk>/update/', DishUpdateAPIView.as_view(), name='dish-update'),   
]