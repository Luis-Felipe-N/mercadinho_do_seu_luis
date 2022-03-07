from django.contrib import admin
from django.urls import path, include
from mercado import urls
import mercado.urls
import users.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(mercado.urls)),
    path('users/', include(users.urls))
]
