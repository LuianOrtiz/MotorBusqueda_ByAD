from django.urls import path
from motor_busqueda import views

urlpatterns = [
    path('', views.index, name='index'),
    path('url_inicial/', views.url_inicial, name='url_inicial'),

]