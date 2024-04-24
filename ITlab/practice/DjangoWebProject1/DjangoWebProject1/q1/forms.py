from django import forms

class CarForm(forms.Form):
    choices = [
        ('Suzuki', 'Suzuki'),
        ('Toyota', 'Toyota'),
        ('Honda', 'Honda'),
    ]
    manufacturer = forms.ChoiceField(label="Car Manufacturer", choices=choices)
    model_name = forms.CharField(label="Model Name",widget=forms.TextInput)
    
class FirstForm(forms.Form):
    choices = [
        ('Math', 'Math'),
        ('Physics', 'Physics'),
        ('Chemistry', 'Chemistry'),
    ]
    name = forms.CharField(label='Name')
    rollno = forms.CharField(label='Roll No.')
    subject = forms.ChoiceField(choices=choices, label='Subject')