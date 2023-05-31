from django.http import HttpResponseBadRequest,HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.views.generic import View
from .forms import *
from .models import *
from django.db.models import Q


def home(request):
    list = Contact.objects.all()
    return render(request, 'contacts/home.html', {'list':list})

def save_number(request):
    list = Contact.objects.all()
    if request.method == "POST":
        form = SaveNumberForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts:save_number')

    else:
        form = SaveNumberForm()
        list = Contact.objects.all()
    return render(request, 'contacts/home.html', {'form': form , 'list': list})

def delete_number(request, contact_id):
    contact_delete = Contact.objects.get(id=contact_id)
    contact_delete.delete()
    return redirect('contacts:save_number')

def change_contact(request, contact_id):
    change_contact = Contact.objects.get(id=contact_id)
    form = SaveNumberForm(instance=change_contact)
    if request.method == 'POST':
        form = SaveNumberForm(request.POST, instance=change_contact)
        if form.is_valid():
            form.save()
            return redirect('contacts:save_number')
    return render(request, 'contacts/home.html', {'form': form , 'list': list})

# def search_contact(name):
#         print('qq')
#         try:
#             contact_name = Contact.objects.get(name = name)
#             print('a')
#             return contact_name
#         except Contact.DoesNotExist:
#             print('s')
#             return None

def search(request):
    results = Contact.objects.filter(Q(name__icontains=request))
    return results



    # try:
    #     person = Contact.objects.get(name=request)
    #     return
    #     print('eeee')
    # except Contact.DoesNotExist:
    #     print('wwqq')
    #     return None
    #





    # name_contact = Contact.objects.filter(name=value)
    # form = SaveNumberForm()
    # if name_contact is not None:
    #     return render(request,'contacts/home.html', {'form':form , 'name_contact' : name_contact })




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




