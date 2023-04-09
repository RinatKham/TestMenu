from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('menu/<slug:menu_id>/', views.menu_list, name='menu'),
    path('', views.home, name = 'test')
]