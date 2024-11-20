from django.urls import path 
from Rendevouz import views



urlpatterns = [
    path('dogs/', views.DogView.as_view(), name='dogs'),
    path('dogs/<int:pk>/' , views.DogView.as_view() , name='specific_dog')
 ]