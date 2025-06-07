from django import forms
from Artwork.models import Comments

class Commentform(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["post","name","subject","email","message"]