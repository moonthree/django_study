from dataclasses import field
from django import forms
from .models import Chatting

class ChattingForm(forms.ModelForm):
    user = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nickname',
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Chat!!',
                'rows': 5,
                'cols': 50,
            }
        )
    )

    class Meta:
        model = Chatting
        fields = '__all__'