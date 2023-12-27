from django.contrib import admin, messages
from .models import Category, News


class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'nomi_ozgartirilgan', 'created_at', 'updated_at']
    
    def nomi_ozgartirilgan(self, inst):
        return inst.id*100

admin.site.register(Category, NewsCategoryAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'matni_ozgartirilgan', 'bolim', 'created_at', 'updated_at']
    list_filter = ['bolim', ]
    search_fields = ['name', 'bolim__name']
    actions = ['counter_action', 'printer_action']
    
    @admin.action(description='Tanlanganlarni sanash')
    def counter_action(modeladmin, request, queryset):
            messages.success(request, f"Siz tanlagan elementlar soni: {len(queryset)}")

    @admin.action(description='Tanlanganlarni chiqarish')
    def printer_action(modeladmin, request, queryset):
        for j in queryset:
            messages.success(request, j.name)

    def matni_ozgartirilgan(self, inst):
        return inst.matn[:30]

admin.site.register(News, NewsAdmin)