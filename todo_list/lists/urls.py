from django.urls import path

from . import views

app_name = 'lists'
urlpatterns = [
    path('', views.home, name='home'),
    path('list/<list_id>/', views.list_detail,
         name='detail'),
]
