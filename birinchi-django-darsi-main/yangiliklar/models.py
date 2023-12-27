from django.db import models


class Category(models.Model):
    id = models.AutoField("id", primary_key=True)
    name = models.CharField("Nomi", max_length=50)

    # for more info
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bo'lim"
        verbose_name_plural = "Bo'limlar"


class News(models.Model):
    id = models.AutoField("id", primary_key=True)
    name = models.CharField("Nomi", max_length=50)
    matn = models.TextField("Matni", max_length=5000)
    bolim = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="news")

    # for more info
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"
