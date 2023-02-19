from django.urls import path
from . import views

app_name = 'main_inst'

urlpatterns = [
    path('', views.CreateInstaData.as_view(), name='create'),
    
]