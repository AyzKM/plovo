from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Order, AdditionDish

class OrderAdminTranslate(TranslationAdmin):
    model = Order

class AdditionDishTranslate(TranslationAdmin):
    model = AdditionDish

admin.site.register(Order, OrderAdminTranslate)
admin.site.register(AdditionDish, AdditionDishTranslate)

# class AdditionDishInline(admin.TabularInline):
#     model = AdditionDish
#     extra = 0

# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('phone', 'dish', 'location', 'status',)
#     list_editable = ("status",)
#     search_fields = ('dish__name', 'location', )
#     list_filter = ('status',)
#     inlines = [AdditionDishInline]

# admin.site.register(Order, OrderAdmin)

# class AdditionDishAdmin(admin.ModelAdmin):
#      list_display = ('dish', 'order', 'created_at', 'updated_at')
#      fields = ('dish', 'order', 'created_at', 'updated_at')
#      readonly_fields = ('created_at', 'updated_at')

# admin.site.register(AdditionDish, AdditionDishAdmin)

