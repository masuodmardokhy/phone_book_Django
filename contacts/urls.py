from django.urls import path
from . import views


app_name = 'contacts'
urlpatterns = [
    path('s/', views.home, name='home'),
    path('', views.save_number, name='save_number'),
    path('delete/<contact_id>', views.delete_number, name='delete_number'),
    path('change/<contact_id>', views.change_contact, name='change_contact'),
    path('search/', views.search, name='search'),

]



# app_name = 'home'
# urlpatterns = [
#     path('', ContactView.as_view())
# ]