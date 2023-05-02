from django import forms
from django.contrib.auth.models import User
from .models import *

class SaveNumberForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'family', 'phone',)







# class ContactModelForm(forms.ModelForm):
#     class Meta:
#         model = ContactModel
#         fields = ['name', 'family', 'phone']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'family': forms.TextInput(attrs={'class': 'form-control'}),
#             'phone': forms.TextInput(attrs={'class': 'form-control'}),
#         }
#         labels = {
#             'name': 'نام',
#             'family': 'نام خانوادگی',
#             'phone': 'تلفن',
#         }





# class UserRegisterFrom(forms.ModelForm):
#     name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'enter user plz'}))
#     family = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'enter email plz'}))
#     phone = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'enter your lastname'}))



