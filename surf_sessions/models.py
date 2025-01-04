from django.db import models
import datetime
from django.contrib.auth.models import User

# Choices for surf session location, wind direction, tide, and rating.
LOCATION = (
    (0, "Langland"),
    (1, "Caswell"),
    (2, "Llangennith"),
    (3, "Oxwich"),
    (4, "Hunts"),
    (5, "Three Cliffs")
)

WIND = (
    (0, "N"),
    (1, "NE"),
    (2, "E"),
    (3, "SE"),
    (4, "S"),
    (5, "SW"),
    (6, "W"),
    (7, "NW")
)

TIDE = (
    (0, "High"),
    (1, "Mid"),
    (2, "Low")
)

RATING = (
    (0, "*"),
    (1, "**"),
    (2, "***"),
    (3, "****"),
    (4, "*****")
)


class Session(models.Model):
    """
    A model representing a surf session logged by a user.

    Attributes:
        user (ForeignKey): Links the session to the user who created it.
        date (DateField): The date of the surf session.
        time (TimeField): The time of the surf session.
        location (IntegerField): The surf location,
        selected from predefined choices.
        wave_height (PositiveIntegerField): Height of the waves
        during the session.
        wind_direction (IntegerField): Wind direction,
        selected from predefined choices.
        wind_speed (PositiveIntegerField): Wind speed during the session
        (in mph).
        tide (IntegerField): Tide level at the time of the session.
        surfboard_used (TextField): Description of the surfboard used.
        notes (TextField): Additional notes about the session (optional).
        rating (IntegerField): User rating for the session (1-5 stars).
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="surf_sessions"
    )

    date = models.DateField(
        default=datetime.date.today
    )

    time = models.TimeField(
        default=datetime.time(0, 0)
    )

    location = models.IntegerField(
        choices=LOCATION,
        default=0
    )

    wave_height = models.PositiveIntegerField()

    wind_direction = models.IntegerField(
        choices=WIND,
        default=0
    )

    wind_speed = models.PositiveIntegerField()

    tide = models.IntegerField(
        choices=TIDE,
        default=0
    )

    surfboard_used = models.TextField(
        blank=True
    )

    notes = models.TextField(
        blank=True
    )

    rating = models.IntegerField(
        choices=RATING,
        default=0
    )

    class Meta:
        """
        Meta options for the Session model.
        """
        ordering = ["-date", "-time"]


    def __str__(self):
        """
        Return a string representation of the session.

        Displays the session date, time, and location
        in a user-friendly format.
        """
        return f"{self.get_location_display()} on {self.date} at {self.time}"
