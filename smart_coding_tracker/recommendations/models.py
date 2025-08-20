from django.db import models

# Create your models here.
class DSAProblemBank(models.Model):
    title = models.CharField(max_length=225)
    link = models.URLField(unique=True)
    topic = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=20)

    def __str__(self):
        return self.title


