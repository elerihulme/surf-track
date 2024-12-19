from django.db import models
import datetime
from django.contrib.auth.models import User

LOCATION = ((0, "Langland"), (1, "Caswell"), (2, "Llangennith"), (3, "Oxwich"), (4, "Hunts"), (5, "Three Cliffs"))
WIND = ((0, "N"), (1, "NE"), (2, "E"), (3, "SE"), (4, "S"), (5, "SW"), (6, "W"), (7, "NW"))
TIDE = ((0, "High"), (1, "Mid"), (2, "Low"))
RATING = ((0, "*"), (1, "**"), (2, "***"), (3, "****"), (4, "*****"))

# Create your models here.
class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="surf_sessions")
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField(default=datetime.time(0, 0))
    location = models.IntegerField(choices=LOCATION, default=0)
    wave_height = models.PositiveIntegerField()
    wind_direction = models.IntegerField(choices=WIND, default=0)
    wind_speed = models.PositiveIntegerField()
    tide = models.IntegerField(choices=TIDE, default=0)
    surfboard_used = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    rating = models.IntegerField(choices=RATING, default=0)

    class Meta:
        ordering = ["date", "time"]