from django import forms
from .models import Movies

class MovoiesForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '세 얼간이'
            }
        ),
    )
    director = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '라지쿠마르 히라니'
            }
        ),
    )
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': '나 얼간이 아니다!',
                'cols': 40,
                'rows': 3,
            }
        ),
    )
    class Meta:
        model = Movies
        fields = '__all__'