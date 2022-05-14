from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta


class Client(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    idClient = models.CharField(max_length=40)
    profession = models.CharField(max_length=40)
    email = models.EmailField()
    pic2 = models.ImageField(blank=True)

    #used in issue book
    def __str__(self):
        return self.user.first_name+'['+str(self.idClient)+']'
    @property
    def get_name(self):
        return self.user.first_name
    @property
    def getuserid(self):
        return self.user.id


class Book(models.Model):
    catchoice= [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biography'),
        ('history', 'History'),
        ('novel', 'Novel'),
        ('fantasy', 'Fantasy'),
        ('thriller', 'Thriller'),
        ('romance', 'Romance'),
        ('scifi','Sci-Fi')
        ]
    name = models.CharField(max_length=30)
    isbn = models.PositiveIntegerField()
    author = models.CharField(max_length=40)
    category = models.CharField(max_length=30,choices=catchoice,default='education')
    nb_exemplaire = models.PositiveIntegerField(default=1)
    pic = models.ImageField(blank=True)


    def __str__(self):
        return str(self.name)+"["+str(self.isbn)+']'


def get_expiry():
    return datetime.today() + timedelta(days=15)


class IssuedBook(models.Model):
    idClient=models.CharField(max_length=130)
    isbn=models.PositiveIntegerField()
    issuedate=models.DateField(auto_now=True)
    expirydate=models.DateField(default=get_expiry)

    def __str__(self):
        return self.idClient
