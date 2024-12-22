from django.contrib import admin
from .models import Session
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Session)
class SessionAdmin(SummernoteModelAdmin):

    list_display = ('user', 'date', 'time', 'location')
    search_fields = ['user__username']
    list_filter = ('date', 'location')
    summernote_fields = ('notes',)

# Register your models here.

