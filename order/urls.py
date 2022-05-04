from django.urls import path
from order import views
from .views import orderDetail, orderHistory

app_name='order'

urlpatterns = [
    path('thanks/<int:order_id>/', views.thanks, name='thanks'),
    path('history/', orderHistory.as_view(), name='order_history'),
    path('<int:order_id>/', orderDetail.as_view(), name='order_detail'),
]