from django.db import models


class Poll(models.Model):
    question = models.CharField("Savol", max_length=100)
    correct_answer = models.CharField("To'g'ri javob", max_length=100)
    options = models.TextField("Variantlar", max_length=500)
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.question[:20]+" | "+self.correct_answer

    class Meta:
        managed = True
        verbose_name = 'Savol'
        verbose_name_plural = 'Savollar'
