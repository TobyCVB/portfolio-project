from django.db import models

class Goal(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
