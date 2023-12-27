from django.contrib import admin
from .models import Kitob
from django.contrib import messages



@admin.register(Kitob)
class KtiobAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "price")
    search_fields = ("desc", "name")
    list_filter = ("price", "name")
    list_editable = ("price", "name")
    actions = ['count_items']


    def description(self, object):
        return object.desc[:30]+"..."
    

    @admin.action
    def count_items(self, request, queryset):
        count = len(queryset)
        
        for object in queryset:
            print(object.name)
            print(object.desc)
            print(object.price)
            print(object.id)
        
        self.message_user(request, f"Siz tanlagan obyektlar soni {count}", messages.WARNING)
