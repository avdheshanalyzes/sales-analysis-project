from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('teamgroup.urls')),  # Include your app URLs here
]
