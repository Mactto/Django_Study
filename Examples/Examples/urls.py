from django.contrib import admin
from django.urls import path, include
import socialExample.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', socialExample.views.home, name='home'),
    #path('ex/', include('templateExample.urls')),
    #path('account/', include('account.urls')),
    path('social/', include('socialExample.urls')),
    path('accounts/', include('allauth.urls')),
]
