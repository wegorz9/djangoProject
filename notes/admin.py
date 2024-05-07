from django.contrib import admin
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'priority', 'created', 'edited']
    list_filter = ['priority', 'author']
    search_fields = ['title', 'content']


admin.site.register(Note, NoteAdmin)
