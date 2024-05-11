from django.contrib import admin

from catalog.models import Category, Product, Contact, Feedback, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category', 'owner', 'is_published',)
    list_filter = ('category', 'owner', 'is_published',)
    search_fields = ('name', 'description',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('pk', 'country', 'city', 'address', 'ein',)
    list_filter = ('country', 'city',)
    search_fields = ('country', 'city', 'ein')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'phone', 'message', 'created_at',)
    list_filter = ('name', 'phone',)
    search_fields = ('message',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'season', 'is_active',)
    list_filter = ('is_active',)
