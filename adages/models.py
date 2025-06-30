from django.db import models

# Create your models here.

class Adage(models.Model):
    adage_id = models.IntegerField()
    adage_text = models.CharField(max_length=200)
    adage_meaning = models.CharField(max_length=200)
    review_status = models.BooleanField(default=False)


