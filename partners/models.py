from django.db import models

class Partner(models.Model):
    company_name = models.CharField(max_length=255)
    description = models.TextField(help_text="Bref profil du partenaire")
    logo = models.ImageField(upload_to='partners/logos/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
