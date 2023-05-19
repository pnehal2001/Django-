from django.urls import path
from . import views

urlpatterns = [
    path('kenmembers/', views.kenmembers, name='kenmembers'),
    path('members/details/<int:id>', views.details, name='details'),
] 
