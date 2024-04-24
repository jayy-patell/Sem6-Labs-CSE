from django.db import models

class AuthorModel(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField()
    class Meta:
        ordering=('fname',)
    
class PublisherModel(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    url = models.URLField()
    class Meta:
        ordering = ("name",)
    
class BookModel(models.Model):
    title = models.CharField(max_length=30)
    pubdate = models.DateField()
    authors = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    publication = models.OneToOneField(PublisherModel, on_delete=models.CASCADE)
    class Meta:
        ordering = ('title',)

# Create your models here.
