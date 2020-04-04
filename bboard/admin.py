from django.contrib import admin

# Register your models here.
from .models import Bb, Bb1, Rubric


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', )
admin.site.register(Bb, BbAdmin)

admin.site.register(Rubric)

class Bb1Admin(admin.ModelAdmin):
    list_display = ('autor','koment','published','declaration')
    list_display_links = ('autor','koment')
    #search_fields = ('title', 'content', )

admin.site.register(Bb1, Bb1Admin)

