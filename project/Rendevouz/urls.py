from django.urls import path 
from . import views


urlpatterns = [
    path('dogs/', views.DogView.as_view(), name='dogs'),
    path('dogs/<int:pk>/' , views.DogView.as_view() , name='specific_dog'),
    path('',views.AppointmentsView.as_view(), name='appointment')
 ]