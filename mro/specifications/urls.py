from django.urls import path
from . import views

app_name = 'specs'

urlpatterns = [
    path('', views.spec_list, name='spec_list'),
    path('<int:id>/', views.spec_detail, name='spec_detail'),
]