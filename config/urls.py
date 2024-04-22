from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # users
    path('user/', include('users.urls')),

    # main
    path('', include('main.urls')),

    # services
    path('services/', include('services.urls')),
]
