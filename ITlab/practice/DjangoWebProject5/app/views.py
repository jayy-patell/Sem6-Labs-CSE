from django.shortcuts import render
from django.http import HttpResponse
from . import models,forms

def index(request):
    if request.method == 'POST':
        feedback_form = forms.FeedbackForm(request.POST)
        if feedback_form.is_valid():
            #feedback = feedback_form.save()
            #feedback.save()
            context = {
                'name': feedback_form.cleaned_data['studname']    
            }
            return render(request,'index.html',{'context': context, 'form': forms.FeedbackForm()})
    return render(request,'index.html',{'form': forms.FeedbackForm()})
    
# Create your views here.
