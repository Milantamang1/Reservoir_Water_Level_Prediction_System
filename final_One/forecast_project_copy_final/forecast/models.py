
# Create your models here.
from django.db import models

class WaterLevelPrediction(models.Model):
    date = models.DateField(auto_now_add=True)  # Automatically stores the current date
    predicted_level = models.FloatField()

    def __str__(self):
        return f"{self.date} - {self.predicted_level}"
