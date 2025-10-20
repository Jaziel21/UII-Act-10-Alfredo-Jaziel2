from django import forms
from .models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'nacionalidad', 'fecha_nacimiento', 'bibliografia', 'pagina_web']
        labels = {
            'nombre': 'Nombre del Autor',
            'apellido': 'Apellido del Autor',
            'nacionalidad': 'Nacionalidad',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'bibliografia': 'Biografía',
            'pagina_web': 'Página Web',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'bibliografia': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'pagina_web': forms.URLInput(attrs={'class': 'form-control'}),
        }