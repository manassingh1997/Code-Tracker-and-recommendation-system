from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Goal(models.Model):
    PERIOD_CHOICES = [('daily', 'Daily'), ('weekly', 'Weekly'),]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target_count = models.IntegerField()
    period = models.CharField(max_length=10, choices=PERIOD_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    