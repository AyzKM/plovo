from django.urls import path
from .views import OrderListCreateView, OrderView

urlpatterns = [
    path('', OrderListCreateView.as_view(), name='order-list-create'),
    path('<int:pk>/', OrderView.as_view(), name='order'),
    # path('<int:pk>/update', OrderView.as_view(), name='order-update'),
    # path('<int:pk>/delete', OrderView.as_view(), name='order-delete'),
]