from django.forms import ModelForm
from .models import PlayTime

class PlayTimeForm(ModelForm):
    class Meta:
        model = PlayTime
        fields = ['date', 'hours_played', 'completed']