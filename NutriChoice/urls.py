from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calculate/', views.calculate_bmi, name='calculate_bmi'),
    path('generate_recipes/', views.generate_recipes, name='generate_recipes'),
]
