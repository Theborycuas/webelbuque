from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Ingresa tu nombre'}
    ), min_length=3, max_length=100)
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Ingresa tu Email'}
    ), min_length=3, max_length=100)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class':'form-control w-100', 'cols':'30', 'rows':'9', 'placeholder':'Ingresa tu mensaje'}
    ), min_length=13, max_length=1000)
    