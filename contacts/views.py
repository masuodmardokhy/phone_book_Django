from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import View
from .forms import *
from .models import *


def home(request):
    list = Contact.objects.all()
    return render(request, 'contacts/home.html', {'list':list})

def save_number(request):
    if request.method == "POST":
        form = SaveNumberForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = SaveNumberForm()
        return render(request, 'contacts/home.html', {'form': form})






# class ContactView(View):
#     def get(self, request:HttpRequest):
#         form = ContactModelForm()
#         context = {
#             'form': form
#         }
#         return render(request,'contacts/home.html',context)
#     def post(self, request:HttpRequest):
#         form = ContactModelForm(request.POST)
#         if form.is_valid():
#             user_name = form.cleaned_data.get('name')
#             user_family = form.cleaned_data.get('family')
#             user_phone = form.cleaned_data.get('phone')
#             user:bool = User.objects.filter(name__iexact=user_name,family__iexact=user_family, phone__iexact=user_phone).exists()
#             # if user is not None:
#             #     if request.user.is_authenticated:
#             #         info_user = User(name=user_name, family=user_family, phone= user_phone)
#             #         info_user.save()
#             #     else:
#             #         return redirect(reverse('home'))
#         else:
#             context = {
#                 'form': form
#             }
#             return render(request, 'contacts/home.html',context)




