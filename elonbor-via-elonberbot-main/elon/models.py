from django.db import models


    # 1. E'lon nomi
    # 1.1 Rasm
    # 2. E'lon turi
    # 3. Aloqa(Contact)
    # 4. Qo'shimcha ma'lumot: 



ELON_TURI = [
    ("KM", "Ko'chmas mulk"),
    ("T", "Transport"),
    ("I", "Ish"),
    ("H", "Hayvonlar"),
    ("UB", "Uy va Bog'"),
]

class Elon(models.Model):
    name = models.CharField("E'lon nomi", max_length=200)
    photo = models.ImageField("Rasmi", upload_to="elon_images")
    etype = models.CharField("Turi", choices=ELON_TURI, max_length=2)
    contact = models.CharField("Aloqa uchun", max_length=13)
    additional_info = models.TextField("Qo'shimcha ma'lumot")


    # some date infos   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self, ):
        return self.name
