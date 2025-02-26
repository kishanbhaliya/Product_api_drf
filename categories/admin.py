from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'is_deleted')
    search_fields = ('name',)
    list_filter = ('parent',)
    # ordering = ('id',)

admin.site.register(Category, CategoryAdmin)
