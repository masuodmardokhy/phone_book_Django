from django.contrib import admin
from .models import *


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'family', 'phone']

admin.site.register(Contact,ContactAdmin)



