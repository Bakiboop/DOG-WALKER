from django.urls import path 
from . import views


urlpatterns = [
    
    path('',views.AppointmentsView.as_view(), name='appointment')
 ]