from .models import Session
from django import forms


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ('user', 'date', 'time', 'location', 'wave_height', 'wind_direction', 'wind_speed', 'tide', 'surfboard_used', 'notes', 'rating')

        labels = {
            'wave_height': 'Wave Height (ft)',
            'wind_speed': 'Wind Speed (mph)',
        }