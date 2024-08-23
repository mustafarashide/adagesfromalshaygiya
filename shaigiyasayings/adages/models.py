from django.db import models

# Create your models here.

class Adage(models.Model):
    adage_text=models.TextField()
    adage_meaning=models.TextField()
    
    def __str__(self):
        return self.adage_text