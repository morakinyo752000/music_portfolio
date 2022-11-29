from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('social/', views.social, name='social'),

]