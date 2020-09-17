from django import forms
from .models import Userupdate
# DataFlair #File_Upload


class Profile_Form(forms.ModelForm):
    class Meta:
        model = Userupdate
        fields = [
            'name',
            'mobile',
            'address',
            'image',

        ]
