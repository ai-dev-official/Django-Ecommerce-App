from django.contrib import admin
from .models import Category, Product, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'category', 'stock', 'voucher', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    list_per_page = 20
""" 
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product', 'user_email', 'user_url', 'body', 'ip_address', 'ip_public', 'is_removed')
    list_filter = ('submit_date','content_type_id', 'site_id', 'object_pk' )
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True) """

admin.site.register(Product, ProductAdmin)