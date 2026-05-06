from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'group', 'answer', 'takeCardNumber',
                 'takeCardCVV', 'takeCardFIO', 'takeCardDATA']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия Имя Отчество'
            }),
            'group': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер группы'
            }),
        }