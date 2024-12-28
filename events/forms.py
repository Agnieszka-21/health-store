from django import forms

from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'when',
            'speaker',
            'description',
            'cancelled',
        ]
        widgets = {
            'when': forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd hh:mm:ss'}),
        }