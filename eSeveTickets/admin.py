from django.contrib import admin
from .models import Item , State, Company
# Register your models here.

admin.site.register(Item)
admin.site.register(State)
admin.site.register(Company)