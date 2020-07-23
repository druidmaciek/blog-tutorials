from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("lists.api.urls", namespace="api")),
    path('', include('lists.urls', namespace='lists')),
]
