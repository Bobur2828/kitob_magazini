from django.contrib import admin
from .models import Book,Category,Izoh,Status,Obuna,Country



@admin.register(Book)
class ookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','avtor','is_active','photo')
    list_display_links = ('name','id')
    ordering = ('name',)
    list_editable=('is_active',)
    list_per_page = 10
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','content' )
    list_display_links = ('name',)
    ordering = ('name',)
    list_per_page = 10

@admin.register(Izoh)
class IzohAdmin(admin.ModelAdmin):
    list_display = ('id','name','content')
    list_display_links = ('name',)
    ordering = ('name',)
    list_per_page = 10

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id','name','content' )
    list_display_links = ('name',)
    ordering = ('name',)
    list_per_page = 10

@admin.register(Obuna)
class ObunaAdmin(admin.ModelAdmin):
    list_display = ('id','name','content' )
    list_display_links = ('name',)
    ordering = ('name',)
    list_per_page = 10


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'slug')
    list_display_links = ('name','slug')
    ordering = ('name',)
    list_per_page = 10






