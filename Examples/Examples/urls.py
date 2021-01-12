from django.contrib import admin
from django.urls import path, include
import account.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', account.views.home, name='home'),
    path('ex/', include('templateExample.urls')),
    path('account/', include('account.urls')),
]
