from django import forms
from . import models

class FeedbackForm(forms.Form):
    CHOICES= [('Male','Male'), ('Female','Female')]
    CHOICES2 = [('ASP-XML','ASP-XML'), ('DotNET','DotNET'), ('JavaPro','JavaPro')]
    CHOICES3 = [('Good','Good'), ('Average','Average'), ('Bad','Bad')]
    
    studname = forms.CharField(max_length=30)
    sex = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    select_course = forms.ChoiceField(choices=CHOICES2, widget=forms.Select)
    technical_confidence = forms.ChoiceField(choices=CHOICES3, widget=forms.RadioSelect)
    suggestions = forms.CharField(max_length=30)