from django.contrib import admin
from .models import Spec


@admin.register(Spec)
class SpecAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'publish']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'description']
    prepopulated_field = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    show_facets = admin.ShowFacets.ALWAYS