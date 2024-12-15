from django.contrib import admin
from .models import Spec, Quality


@admin.register(Spec)
class SpecAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'publish']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    show_facets = admin.ShowFacets.ALWAYS


@admin.register(Quality)
class QualityAdmin(admin.ModelAdmin):
    list_display = ['spec', 'name', 'test_spec', 'description', 'status', 'publish']
    prepopulated_fields = {'slug': ('name',)}