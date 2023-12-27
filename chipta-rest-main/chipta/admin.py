from django.contrib import admin
from .models import (Bekat, Poyezd, Vagon, Yonalish, Chipta, Mijoz)


@admin.register(Bekat)
class BekatAdmin(admin.ModelAdmin):
    list_display = ("id", "nomi", 
        "chiquvchi_qatnovlar", "kiruvchi_qatnovlar")
    
    def chiquvchi_qatnovlar(self, obj):
        return obj.qayerdan.all().count()

    def kiruvchi_qatnovlar(self, obj):
        return obj.qayerga.all().count()


@admin.register(Vagon)
class VagonAdmin(admin.ModelAdmin):
    list_display = ("id", "raqami", "turi",
                "poyezd", "joylar_soni", "narxi")
    
@admin.register(Poyezd)
class PoyezdAdmin(admin.ModelAdmin):
    list_display = ("id", "nomi", "vagonlar_soni")

    def vagonlar_soni(self, obj):
        return obj.vagonlar.all().count()
    
    def bekatlar_soni(self, obj):
        return obj.vagonlar.all().count()



@admin.register(Yonalish)
class YonalishdAdmin(admin.ModelAdmin):
    list_display = ("nomi", "poyezd", "qayerdan", 
        "qayerga", "jonash_vaqti", "davomiyligi") 
    
    
@admin.register(Mijoz)
class MijozdAdmin(admin.ModelAdmin):
    list_display = ("user_id", "user_firstname", "phone_number") 

    def user_id(self, x): return x.user.id
    def user_firstname(self, x): return x.user.first_name

@admin.register(Chipta)
class ChiptaAdmin(admin.ModelAdmin):
    list_display = ("id", "mijoz_detail", "yonalish",
                    "sotilgan_vaqti", "turi", "narxi",
                    "joy_raqami")
    
    def mijoz_detail(self, x): return f"{x.mijoz.first_name} {x.mijoz.last_name} | {x.mijoz.mijoz.phone_number}"
    
    def turi(self, obj):
        return obj.vagon.turi

    
    def narxi(self, obj):
        return obj.vagon.narxi