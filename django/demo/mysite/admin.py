from django.contrib import admin
from models import *



class DocAdmin(admin.ModelAdmin):
    list_display = ('id', 'dsubject', 'contents','writer',)
    search_fields = ('name','writer')
admin.site.register(Doc, DocAdmin)