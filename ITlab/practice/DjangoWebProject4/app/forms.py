from django import forms
from . import models

class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.AuthorModel
        exclude = ()

class PublisherForm(forms.ModelForm):
    class Meta:
        model = models.PublisherModel
        exclude = ()
        
class BookForm(forms.ModelForm):
    pubdate = forms.DateField(input_formats=['%d/%m/%Y'])
    class Meta:
        model = models.BookModel
        exclude = ()