from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import models, forms

def index(request):
    pages = models.PageModel.objects.all()
    categories = models.CategoryModel.objects.all()
    return render(request,'index.html',{"categories": categories, "pages": pages, 
                                        "cat_form": forms.CategoryForm(), "page_form": forms.PageForm()})

def create(request):
    if request.method == 'POST':
        cat_form = forms.CategoryForm(request.POST)
        page_form = forms.PageForm(request.POST)
        if cat_form.is_valid() and page_form.is_valid():
            cat = cat_form.save(commit=False)
            page = page_form.save()
            cat.save()
            page.save()
        return HttpResponseRedirect('/')



# Create your views here.
