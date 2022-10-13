from django.contrib import admin
from .models import Person

@admin.register(Person)
class AuthorAdmin(admin.ModelAdmin):
    list_display= ['id', 'first_name', 'last_name', 'age']
