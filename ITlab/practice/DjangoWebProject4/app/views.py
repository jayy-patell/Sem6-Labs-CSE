from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import models, forms

def index(req):
    publishers = models.PublisherModel.objects.all()
    books = models.BookModel.objects.all()
    authors = models.AuthorModel.objects.all()
    return render(req,'book.html',{'publishers':publishers, 'authors': authors, 'books': books,
                                    'publisher_form': forms.PublisherForm(), 'author_form': forms.AuthorForm(),
                                   'book_form': forms.BookForm()})

def create(req):
    if req.method == 'POST':
        publisher_form = forms.PublisherForm(req.POST)
        author_form = forms.AuthorForm(req.POST)
        if publisher_form.is_valid() and author_form.is_valid():
            publisher = publisher_form.save()
            author = author_form.save()
            publisher.save()
            author.save()
        else:
            print("error")
            print("Authors Valid : ", author_form.is_valid())
            print("Publisher Valid : ", publisher_form.is_valid())
            
        if not author_form.is_valid():
            return render(req, 'err.html', {'form': author_form})
        elif not publisher_form.is_valid():
            return render(req, 'err.html', {'form': publisher_form})
        
        return HttpResponseRedirect('/')
    
def createbook(req):
    if req.method == 'POST':
        book_form = forms.BookForm(req.POST)
        if book_form.is_valid():
            book = book_form.save(commit=False)
            book.save()
        else:
            print("ERROR")
            print("Book Valid : ", book_form.is_valid())
        if not book_form.is_valid():
            return render(req, 'err.html', {'form': book_form})

    return HttpResponseRedirect('/')

# Create your views here.
