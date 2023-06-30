from django import forms
from .models import *
from moviepy.editor import TextClip


class CreateVideoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Ticker
        fields = ['message', 'duration', 'bg_color', 'text_color']
        widgets = {
            'duration': forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '1', 'max': '15', 'class': 'slider', 'value': '3'}),
            'bg_color': forms.TextInput(attrs={'class': 'form-input', 'value': 'black'}),
            'text_color': forms.TextInput(attrs={'class': 'form-input', 'value': 'white'}),
        }


    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) > 500:
            raise forms.ValidationError("Введите текст покороче. Максимальная длина - 500 символов")
        return message
    
    def clean_bg_color(self):
        bg_color = self.cleaned_data['bg_color']
        colors = [el.decode("utf-8") for el in TextClip.list('color')]
        if bg_color not in colors:
            raise forms.ValidationError("Некорректный цвет заднего фона")
        return bg_color
    
    def clean_text_color(self):
        text_color = self.cleaned_data['text_color']
        colors = [el.decode("utf-8") for el in TextClip.list('color')]
        if text_color not in colors:
            raise forms.ValidationError("Некорректный цвет текста")
        return text_color