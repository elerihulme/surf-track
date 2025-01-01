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
        location (IntegerField): The surf location, selected from predefined choices.
        wave_height (PositiveIntegerField): Height of the waves during the session.
        wind_direction (IntegerField): Wind direction, selected from predefined choices.
        wind_speed (PositiveIntegerField): Wind speed during the session (in mph).
        tide (IntegerField): Tide level at the time of the session.
        surfboard_used (TextField): Description of the surfboard used (optional).
        notes (TextField): Additional notes about the session (optional).
        rating (IntegerField): User rating for the session (1-5 stars).
    """

    # Link the session to the user who created it. If the user is deleted, the session is also deleted.
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="surf_sessions"
    )

    # Date of the surf session; defaults to today's date.
    date = models.DateField(
        default=datetime.date.today
    )

    # Time of the surf session; defaults to midnight (00:00).
    time = models.TimeField(
        default=datetime.time(0, 0)
    )

    # Location of the surf session, selected from predefined choices; defaults to the first location (Langland).
    location = models.IntegerField(
        choices=LOCATION, 
        default=0
    )

    # Height of the waves in feet (positive values only).
    wave_height = models.PositiveIntegerField()

    # Wind direction during the surf session, selected from predefined choices; defaults to the first direction (North).
    wind_direction = models.IntegerField(
        choices=WIND, 
        default=0
    )

    # Wind speed in mph during the session (positive values only).
    wind_speed = models.PositiveIntegerField()

    # Tide condition during the session, selected from predefined choices; defaults to the first option (High).
    tide = models.IntegerField(
        choices=TIDE, 
        default=0
    )

    # Description of the surfboard used, can be left blank.
    surfboard_used = models.TextField(
        blank=True
    )

    # Additional notes or observations about the surf session, can be left blank.
    notes = models.TextField(
        blank=True
    )

    # User rating of the session (1 to 5 stars), selected from predefined choices; defaults to the first option (1 star).
    rating = models.IntegerField(
        choices=RATING, 
        default=0
    )

    class Meta:
        """
        Meta options for the Session model.
        """
        # Order sessions by date and time (latest first).
        ordering = ["-date", "-time"]

    def __str__(self):
        """
        Return a string representation of the session.
        
        Displays the session date, time, and location in a user-friendly format.
        """
        return f"{self.get_location_display()} on {self.date} at {self.time}"