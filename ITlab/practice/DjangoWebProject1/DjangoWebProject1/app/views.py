from django.shortcuts import render
from app.forms import GeeksForm, RegForm, LoginForm
from django.http import HttpResponse


def reg_form_view(request):
    context = {}
    form = RegForm(request.POST)
    context['form'] = form
    return render(request, 'index.html', context)


def geek_form_view(request):
    context = {}
    form = GeeksForm()
    context['form'] = form
    return render(request, 'index.html', context)


def login(request):
    username = "not logged in"    
    cn = "not found"    
    if request.method == "POST":  
        MyLoginForm = LoginForm(request.POST)          
        if MyLoginForm.is_valid():  
            username = MyLoginForm.cleaned_data['username']           
            cn= MyLoginForm.cleaned_data['contact_num']
            request.session['username'] = username
            print(request.session)
        else:  
            MyLoginForm = LoginForm()  
    context = {'username': username, 'contact_num': cn} 
    if request.session.has_key('username'): 
        username = request.session['username']
        return render(request, 'loggedin.html', {'context':context, "username" : username}) 
    else:
        return render(request, 'login.html', { })


def login_page(request):
    return render(request, 'login.html')


# def login(request): 
#     username = 'not logged in' 
#     if request.method == 'POST':
#         MyLoginForm = LoginForm(request.POST) 
#         if MyLoginForm.is_valid():
#             username = MyLoginForm.cleaned_data['username'] 
#             request.session['username'] = username 
#         else:
#             MyLoginForm = LoginForm()
#         return render(request, 'loggedin.html', {"username" : username})


def formView(request): 
    if request.session.has_key('username'): 
        username = request.session['username']
        return render(request, 'loggedin.html', {"username" : username}) 
    else:
        return render(request, 'login.html', { })


def logout(request): 
    try:
        del request.session['username'] 
    except: 
        pass
    return HttpResponse("<strong>You are logged out</strong>")
    

# Create your views here.
