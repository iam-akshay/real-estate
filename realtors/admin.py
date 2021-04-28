from django.contrib import admin
from .models import Realtor

@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'is_mvp', 'hire_date')
    list_per_page = 25
    list_editable = ('is_mvp',)
    list_filter = ('is_mvp',)
    search_fields = ('name', 'phone', 'email', 'hire_date')
