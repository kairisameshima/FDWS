
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('walk_scheduler/', include('walk_scheduler.urls')),
    path('admin/', admin.site.urls),
]
