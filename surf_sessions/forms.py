from .models import Session
from django import forms
import datetime


class SessionForm(forms.ModelForm):
    """
    Form for creating and editing surf session entries.
    
    This form uses the Session model and allows users to input details 
    about their surf sessions, such as date, time, location, and wave conditions.
    """
    class Meta:
        """
        Meta class to define model, fields, labels and widgets for the form.
        """
        model = Session
        fields = (
            'date', 
            'time', 
            'location', 
            'wave_height', 
            'wind_direction', 
            'wind_speed', 
            'tide', 
            'surfboard_used', 
            'notes', 
            'rating'
            )

        # Custom labels for better user readability in the form
        labels = {
            'wave_height': 'Wave Height (ft)',
            'wind_speed': 'Wind Speed (mph)',
            'rating': 'Wave Rating (1-5)'
        }

        # Widgets for customizing field rendering
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'surfboard_used': forms.TextInput(attrs={'placeholder': 'Enter surfboard model'})
        }

    def clean_date(self):
        """
        Validate the date field to ensure that the session cannot be logged in the future.

        Returns:
            date: The cleaned and validated date input.

        Raises:
            forms.ValidationError: If the date is in the future.
        """
        # Get the date from the form data
        date = self.cleaned_data['date']
        # Check if the date is in the future
        if date > datetime.date.today():
            raise forms.ValidationError("You cannot log a surf session in the future.")
        # Return the valid date
        return date

    def clean_wave_height(self):
        """
        Validate the wave height to ensure it is within a reasonable range.

        Returns:
            wave_height: The cleaned and validated wave height input.

        Raises:
            forms.ValidationError: If the wave height is negative or exceeds 100 feet.
        """
        wave_height = self.cleaned_data['wave_height']

        if wave_height < 0:
            raise forms.ValidationError("Wave height cannot be negative.")
        if wave_height > 100:
            raise forms.ValidationError("Wave height cannot exceed 100 feet.")
        
        return wave_height

    def clean_wind_speed(self):
        """
        Validate the wind speed to ensure it is within a reasonable range.

        Returns:
            wind_speed: The cleaned and validated wind speed input.

        Raises:
            forms.ValidationError: If the wind speed is negative or exceeds 100 mph.
        """
        wind_speed = self.cleaned_data['wind_speed']

        if wind_speed < 0:
            raise forms.ValidationError("Wind speed cannot be negative.")
        if wind_speed > 100:
            raise forms.ValidationError("Wind speed cannot exceed 100 mph.")
        
        return wind_speed