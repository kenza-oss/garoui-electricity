from django.db import models

class Employee(models.Model):
    first_name = models.CharField("Prénom", max_length=100)
    last_name = models.CharField("Nom", max_length=100)
    role = models.CharField("Poste", max_length=150, help_text="ex: Technicien supérieur")
    address = models.CharField("Adresse", max_length=200, help_text="ex: BIRTOUTA, ALGER")
    profile_photo = models.ImageField("Photo de profil", upload_to='team/profiles/')
    experience = models.TextField("Expérience", help_text="Saisissez une expérience par ligne (elles seront affichées sous forme de puces)")
    work_done = models.TextField("Travaux réalisés", help_text="Saisissez un travail par ligne (elles seront affichées sous forme de puces)")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role}"

    class Meta:
        verbose_name = "Employé"
        verbose_name_plural = "Employés"

class EmployeeWorkImage(models.Model):
    employee = models.ForeignKey(Employee, related_name='work_images', on_delete=models.CASCADE)
    image = models.ImageField("Image de réalisation", upload_to='team/work/')

    def __str__(self):
        return f"Image pour {self.employee}"
        
    class Meta:
        verbose_name = "Image de travail"
        verbose_name_plural = "Images de travaux"
