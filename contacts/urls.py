from django.urls import path
from contacts.views import *
from . import views


app_name = 'contacts'
urlpatterns = [
    path('', views.home, name='home'),
    path('save/', views.save_number, name='save_number'),

]


# app_name = 'home'
# urlpatterns = [
#     path('', ContactView.as_view())
# ]