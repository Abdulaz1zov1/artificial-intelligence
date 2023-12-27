from django.db import models


class Kitob(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=2000)
    price = models.IntegerField()

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"

    def __str__(self):
        return self.name
