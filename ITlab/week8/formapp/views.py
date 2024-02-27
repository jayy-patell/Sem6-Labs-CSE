from django.shortcuts import render 
from formapp.forms import LoginForm 

def index(request): 
    return render(request, 'login.html') 

def login(request): 
    username = "not logged in"
    cn="not found" 
    if request.method == "POST": 
        #Get the posted form 
        MyLoginForm = LoginForm(request.POST) 
        if MyLoginForm.is_valid(): 
            username = MyLoginForm.cleaned_data['username']
            cn=MyLoginForm.cleaned_data['contact_num'] 
        else: 
             MyLoginForm = LoginForm() 
    context = {'username': username,'contact_num':cn} 
    
    return render(request, 'loggedin.html',context) 