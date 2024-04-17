from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models,forms

def first(request):
    employees = models.Employee.objects.all()
    return render(request, 'first.html', {'employees': employees})

def second(request):
    return render(request, 'second.html', {'empform': forms.EmployeeForm()})

def add(request):
    if request.method == 'POST':
        form = forms.EmployeeForm(request.POST)
        print(request.POST)
        if form.is_valid():
            salary = int(form.cleaned_data['salary'])
            print(salary)
            if salary > 10000:
                return render(request, 'second.html', {'empform': form, 'error': 'Salary should be greater than 10000'})
            form.save()
    else:
        form = forms.EmployeeForm()
        return render(request, 'add.html', {'form': form})
    return HttpResponseRedirect('/first/')

def delete(request, name):
    if request.method == 'POST':
        models.Employee.objects.filter(name=name).delete()
        return HttpResponseRedirect('/first/')

# Create your views here.
