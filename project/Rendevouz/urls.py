from django.urls import path 
from . import views


urlpatterns = [
    
    path('appointments/',views.AppointmentsView.as_view(), name='appointment')
 ]