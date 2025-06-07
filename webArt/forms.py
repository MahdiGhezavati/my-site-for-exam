from django import forms
from webArt.models import Contact 
from captcha.fields import CaptchaField

class Contactform(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        exclude = ["name"]