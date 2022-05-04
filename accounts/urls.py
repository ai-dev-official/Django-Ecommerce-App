from django.urls import path
from . import views
from .views import signin, signout, UserEditView, get_or_create_profile, signup

app_name = 'accounts'

urlpatterns = [
    # path('create/', signout, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', signout, name='signout'),
    path('signup/', signup, name='signup'),
    path('edit_profile/<int:pk>/', UserEditView.as_view(), name='edit_profile'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path("dashboard", views.dashboard, name="dashboard"),
    path('userpage/', get_or_create_profile, name='userpage'),
    # path('profile/<int:pk>/', ProfilePageView.as_view(), name='show_profile'),
    path("wishlist", views.wishlist, name="wishlist"),
    path('wishlist/add_to_wishlist/<int:id>',
         views.add_to_wishlist, name='user_wishlist'),
    # path("userpage/", userpageView, name="userpage"),
]
