from django.db import models

# Create your models here.

# Clasa Firma
class Firma(models.Model):
    name = models.CharField(max_length=100)                 # Nume firma
    logo = models.ImageField(upload_to='firme_logos')       # Logo firma
    pdf = models.FileField(upload_to='firme_pdfs')          # PDF firma

    def __str__(self):
        return self.name                                    # Afiseaza "Nume_Firma"

    class Meta:
        verbose_name = 'Firma'
        verbose_name_plural = 'Firme'


# Clasa Utilaj de vanzare
# M:1 cu Firma
# Doar utilajele de vanzare aprtin unei firme
# Utilajele de vanzare au mai multe poze
class UtilajVanzare(models.Model):
    name = models.CharField(max_length=100)                             # Nume utilaj de vanzare
    pdf = models.FileField(upload_to='utilaje_vanzare_pdfs')            # Pdf utilaj de vanzare
    firma = models.ForeignKey(Firma, on_delete=models.CASCADE, related_name='utilaje_vanzare')          # Firma utilaj de vanzare

    def __str__(self):
        return f"{self.firma.name} {self.name}"                   # Afiseaza "Nume_Firma Nume_Utilaj"

    class Meta:
        verbose_name = 'Utilaj de Vanzare'
        verbose_name_plural = 'Utilaje de Vanzare'


# Clasa Imagini Utilaj Vanzare
# M:1 cu UtilajVanzare
class UtilajVanzareImage(models.Model):
    image = models.ImageField(upload_to='utilaje_vanzare_images')                                               # Imagine utilaj de vanzare
    utilaj = models.ForeignKey(UtilajVanzare, on_delete=models.CASCADE, related_name='utilaj_vanzare_image')    # Utilajul de vanzare

    def __str__(self):
        return self.utilaj.name                                                                             # Afiseaza "Nume_Firma Nume_Utilaj"

    class Meta:
        verbose_name = 'Imagine Utilaj de Vanzare'
        verbose_name_plural = 'Imagini Utilaj de Vanzare'                                  


# Clasa Utilaj Propriu
# Utilaj Propriu are o singura poza
class UtilajPropriu(models.Model):
    name = models.CharField(max_length=100)                       # Nume utilaj propriu
    image = models.ImageField(upload_to='utilaje_proprii_images') # Imagine utilaj propriu
    
    def __str__(self):
        return self.name                                          # Afiseaza "Nume_Utilaj_Propriu'

    class Meta:
        verbose_name = 'Utilaj Propriu'
        verbose_name_plural = 'Utilaje Proprii'


# Clasa Descriere Utilaj Vanzare
# M:1 cu UtilajVanzare
class UtilajVanzareDescription(models.Model):
    description = models.TextField()                                                                                # Descriere Utilaj Vanzare                                                                                          
    utilaj = models.ForeignKey(UtilajVanzare, on_delete=models.CASCADE, related_name='utilaj_vanzare_descriptions') # Utilajul de Vanzare

    def __str__(self):
        return self.utilaj.name                                                                                 # Afiseaza "Nume_Firma Nume_Utilaj"

    class Meta:
        verbose_name = 'Descriere Utilaj de Vanzare'
        verbose_name_plural = 'Descrieri Utilaj de Vanzare'


# Clasa Descriere Utilaj Propriu
# M:1 cu UtilajPropriu
class UtilajPropriuDescription(models.Model):
    description = models.TextField()                                                                                # Descriere Utilaj Propriu                                                                                        
    utilaj = models.ForeignKey(UtilajPropriu, on_delete=models.CASCADE, related_name='utilaj_propriu_descriptions') # Utilajul de Propriu

    def __str__(self):
        return self.utilaj.name                                                                                 # Afiseaza "Nume_Firma Nume_Utilaj"

    class Meta:
        verbose_name = 'Descriere Utilaj Propriu'
        verbose_name_plural = 'Descrieri Utilaj Propriu'

##########################################################################################################################################
##########################################################################################################################################


# class Utilaj(models.Model):
#     name = models.CharField(max_length=100)
#     for_sale = models.BooleanField(default=False)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = 'Utilaj'
#         verbose_name_plural = 'Utilaje'


# class UtilajImage(models.Model):
#     image = models.ImageField(upload_to='utilaje')
#     utilaj = models.ForeignKey(Utilaj, on_delete=models.CASCADE, related_name='utilaj_image')

#     def __str__(self):
#         return self.utilaj.name

#     class Meta:
#         verbose_name = 'Imagine Utilaj'
#         verbose_name_plural = 'Imagini Utilaje'


# class UtilajDescription(models.Model):
#     description = models.TextField()
#     utilaj = models.ForeignKey(Utilaj, on_delete=models.CASCADE, related_name='utilaj_descriptions')

#     def __str__(self):
#         return self.utilaj.name

#     class Meta:
#         verbose_name = 'Descriere Utilaj'
#         verbose_name_plural = 'Descriere Utilaje'


# class UtilajCaracteristici(models.Model):
#     logo = models.ImageField(upload_to='logos')
#     pdf = models.FileField(upload_to='pdfs')
#     utilaj = models.ForeignKey(Utilaj, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.utilaj.name

#     class Meta:
#         verbose_name = 'Caracteristici Utilaj'
#         verbose_name_plural = 'Caracteristici Utilaje'