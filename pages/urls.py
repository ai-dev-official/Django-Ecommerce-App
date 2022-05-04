from django.urls import include, path
from .views import HomePageView


app_name = 'pages'


urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
]
