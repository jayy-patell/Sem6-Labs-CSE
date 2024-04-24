from django.shortcuts import redirect, render
from .forms import CarForm, FirstForm
from django.http import HttpResponse


def q1(request):
    form = CarForm()
    return render(request, 'q1.html', {'form':form})


def q1newpage(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            context = {
                'manufacturer': form.cleaned_data['manufacturer'],
                'model_name': form.cleaned_data['model_name'],
            }
            return render(request, 'q1newpage.html', context)
    return HttpResponse("Invalid Parameters")

def q2(request):
    context = {
        'name': None,
        'rollno': None,
        'subject': None,
    }
    if request.method == 'POST':
        ff = FirstForm(request.POST)
        if ff.is_valid():
            context = {
                'name': ff.cleaned_data['name'],
                'rollno': ff.cleaned_data['rollno'],
                'subject': ff.cleaned_data['subject'],
            }
            print(context)
            request.session['context'] = context
            return redirect('/q1/q2newpage/')
    ff = FirstForm()
    return render(request, 'q2.html', {'form': ff})

def q2newpage(request):
    if request.method == 'POST':
        del request.session['context']
        return redirect('/q1/q2/')

    if request.session.has_key('context'):
        return render(request, 'q2newpage.html', {'context':request.session['context']})
    
    return render(request, 'q2newpage.html', {})
    
        

# Create your views here.
