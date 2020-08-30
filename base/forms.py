from django import forms
from django.core.validators import RegexValidator


class form1(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Your email', max_length=150)


class form2(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Your email', max_length=150)
    pregex = RegexValidator(
        regex=r'^\+?1?\d{10,12}$', message="In the format +999999999999")
    t_contact = forms.CharField(validators=[pregex], max_length=17)
    t_subject = forms.CharField(max_length=150)
