from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CodingLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date =models.DateField()
    platform = models.CharField(max_length=50)
    problem_link = models.URLField()
    topic = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=20)
    result = models.CharField(max_length=20)
    notes = models.TextField(blank=True, null=True)