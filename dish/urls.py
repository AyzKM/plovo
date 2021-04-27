from django.urls import path
from dish.views import DishListAPIView

urlpatterns = [
    path('', DishListAPIView.as_view(), name='dishes'),
]