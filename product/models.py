from django.db import models

# Create your models here.
class Utilaj(models.Model):
    name = models.CharField(max_length=100)
    for_sale = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Utilaj'
        verbose_name_plural = 'Utilaje'


class UtilajImage(models.Model):
    image = models.ImageField(upload_to='utilaje')
    utilaj = models.ForeignKey(Utilaj, on_delete=models.CASCADE, related_name='utilaj_image')

    def __str__(self):
        return self.utilaj.name

    class Meta:
        verbose_name = 'Imagine Utilaj'
        verbose_name_plural = 'Imagini Utilaje'


class UtilajDescription(models.Model):
    description = models.TextField()
    utilaj = models.ForeignKey(Utilaj, on_delete=models.CASCADE, related_name='utilaj_descriptions')

    def __str__(self):
        return self.utilaj.name

    class Meta:
        verbose_name = 'Descriere Utilaj'
        verbose_name_plural = 'Descriere Utilaje'


class UtilajCaracteristici(models.Model):
    logo = models.ImageField(upload_to='logos')
    pdf = models.FileField(upload_to='pdfs')
    utilaj = models.ForeignKey(Utilaj, on_delete=models.CASCADE)

    def __str__(self):
        return self.utilaj.name

    class Meta:
        verbose_name = 'Caracteristici Utilaj'
        verbose_name_plural = 'Caracteristici Utilaje'