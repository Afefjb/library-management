from django import forms
from django.contrib.auth.models import User
from . import models


class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))


class AdminSigupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class ClientUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class ClientForm(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = ['idClient', 'email', 'profession','pic2']


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ['name', 'isbn', 'author', 'category', 'nb_exemplaire', 'pic']


class IssuedBookForm(forms.Form):
    #class meta:
     #   unique_together = ('isbn', 'idClient')
    # to_field_name value will be stored when form is submitted.....__str__ method of book model will be shown there in html
    isbn2 = forms.ModelChoiceField(queryset=models.Book.objects.all(), empty_label="Name and isbn",
                                   to_field_name="isbn", label='Name and Isbn')
    idClient2 = forms.ModelChoiceField(queryset=models.Client.objects.all(), empty_label="Name and idClient",
                                         to_field_name='idClient', label='Name and idClient')
class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']

class UpdateProfileForm(forms.ModelForm):
        profession= forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
        idCLient = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

        email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))


        class Meta:
                model =  models.Client
                fields =['idClient', 'email', 'profession']