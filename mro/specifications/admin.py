from django.contrib import admin
from .models import Spec, Quality, Classification, Manual, Solution, ProcessRequired


@admin.register(Spec)
class SpecAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status', 'publish']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    show_facets = admin.ShowFacets.ALWAYS

@admin.register(Classification)
class ClassificationAdmin(admin.ModelAdmin):
    list_display = ['spec', 'classification', 'status', 'publish']


@admin.register(ProcessRequired)
class ProcessRequiredAdmin(admin.ModelAdmin):
    list_display = ['classification', 'process_identity', 'step', 'title', 'status', 'publish']