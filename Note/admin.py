from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}


# Register your models here.
