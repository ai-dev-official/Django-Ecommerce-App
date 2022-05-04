from django.urls import path
from . import views
from .views import ProdCat, ProdDetail

app_name = 'shop'

urlpatterns = [
    path('', ProdCat.as_view(), name='allProdCat'),
    path('<int:category_id>/', ProdCat.as_view(), name='product_by_category'),
    path('<int:category_id>/<int:product_id>/', ProdDetail.as_view(), name='prod_detail'),
    path('subcat/', views.subcat, name='subcat'),
]