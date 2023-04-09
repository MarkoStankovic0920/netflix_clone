from django.urls import path
from .views import Home_view
app_name = 'core'

urlpatterns = [
    path('',Home_view.as_view(),name='home'),



]