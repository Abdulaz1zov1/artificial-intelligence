from django.db import models
from django.contrib.auth.models import User


class Mijoz(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=9)


class Bekat(models.Model):
    nomi = models.CharField('Nomi', max_length=50)

    def __str__(self):
        return self.nomi


class Poyezd(models.Model):
    nomi = models.CharField('Nomi', max_length=50)

    def __str__(self):
        return self.nomi


class Vagon(models.Model):
    turlari = (
        ("U", "Umumiy"),
        ("P", "Plaskart"),
        ("K", "Kupe"),
        ("L", "Lux"),
    )
    
    raqami = models.CharField('Raqami', max_length=50)
    poyezd = models.ForeignKey(to=Poyezd, on_delete=models.CASCADE,
                        related_name="vagonlar")
    turi = models.CharField('Turi', choices=turlari,
                        max_length=1, default="U")
    joylar_soni = models.IntegerField("Joylar soni")
    narxi = models.IntegerField()

    def __str__(self):
        return f"{self.poyezd}, {self.turi} № {self.raqami}"


class Yonalish(models.Model):
    nomi = models.CharField('Nomi', max_length=50)
    poyezd = models.ForeignKey(verbose_name='Poyezd', to=Poyezd, 
                    on_delete=models.CASCADE, related_name="yonalish")
    qayerdan = models.ForeignKey(verbose_name='Qayerdan', to=Bekat, 
                    on_delete=models.CASCADE, related_name="qayerdan")
    qayerga = models.ForeignKey(verbose_name='Qayerga', to=Bekat, 
                    on_delete=models.CASCADE, related_name="qayerga")
    jonash_vaqti = models.DateTimeField()
    davomiyligi = models.TimeField("Davomiyligi")
    


    def __str__(self):
        return self.nomi + " | " + str(self.jonash_vaqti)+"+5h"


class Chipta(models.Model):
    mijoz = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name="chiptalar")
    yonalish = models.ForeignKey(to=Yonalish, on_delete=models.CASCADE,
            related_name="mijoz")
    vagon = models.ForeignKey(to=Vagon, on_delete=models.CASCADE, 
            related_name="mijoz")
    joy_raqami = models.IntegerField()
    sotilgan_vaqti = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.mijoz.mijoz.phone_number) + " | " + str(self.yonalish) + " | " + str(self.joy_raqami)
