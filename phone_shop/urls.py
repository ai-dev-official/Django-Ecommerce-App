# from django import urls
# from django.conf.urls import url
from django.urls import include, re_path
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
#from django.conf.urls import static
#from django.conf.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('search/', include('search_app.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('vouchers/', include('vouchers.urls')),
    path('pages/', include('pages.urls')),
    path('comments/', include('django_comments.urls')),
    # path('ratings/', include('star_ratings.urls')),
    re_path(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
