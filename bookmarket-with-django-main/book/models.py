from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=100)
    desc = models.TextField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "Muallif"
        verbose_name_plural = "Mualliflar"
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Bo'lim"
        verbose_name_plural = "Bo'limlar"


class Book(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=1000)
    author = models.ForeignKey(Author, 
                        on_delete=models.CASCADE)
    category = models.ForeignKey(Category, 
                        on_delete=models.CASCADE)
    price = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"
