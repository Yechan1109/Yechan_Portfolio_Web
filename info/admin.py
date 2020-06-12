from django.contrib import admin
from .models import Client
# Register your models here.

# @admin.register(Client)
# class ClientAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Client._meta.get_fields()]
#     list_display_links = ('name',)