from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from . import forms,models
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group, User
from django.contrib import auth
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.core.mail import send_mail
from librarymanagement.settings import EMAIL_HOST_USER
from .forms import BookForm, UpdateUserForm, UpdateProfileForm
from .models import Book, IssuedBook , Client


def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'library/index.html')

#for showing signup/login button for student
def Clientclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'library/Clientclick.html')

#for showing signup/login button for teacher
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'library/adminclick.html')



def adminsignup_view(request):
    form=forms.AdminSigupForm()
    if request.method=='POST':
        form=forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()


            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)

            return HttpResponseRedirect('adminlogin')
    return render(request,'library/adminsignup.html',{'form':form})









def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def addClient_view(request):
    form1=forms.ClientUserForm()
    form2=forms.ClientForm()
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.ClientUserForm(request.POST)
        form2=forms.ClientForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
            f2.user=user
            user2=f2.save()

            my_student_group = Group.objects.get_or_create(name='CLIENT')
            my_student_group[0].user_set.add(user)

        return render(request, 'library/Clientaded.html')
    return render(request,'library/addClient.html',context=mydict)

def ClientUpdate(request, pk):
    obj = Client.objects.get(user_id=request.user.id)
    obj2 = User.objects.get(user_id=request.user.id)

    form2 = forms.ClientForm(instance=obj)
    form1=forms.ClientUserForm(instance=obj2)
    mydict={'form1':form1,'form2':form2}
    if request.method == 'POST':
        form1 = forms.ClientForm(data=request.POST, instance=obj)
        form2 = forms.ClientUserForm(data=request.POST, instance=obj)
        if form1.is_valid() and form2.is_valid():
            obj1 = form1.save(commit=False)
            obj2 = form2.save(commit=False)
            obj1.save()
            obj2.save()
            return render(request,'library/Clientupdated.html')
    return render(request,'library/updateclient.html',context=mydict)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def ClientUpdate(request, pk):
    obj = Client.objects.get(id=pk)
    obj2 = User.objects.get(id=pk)

    form2 = forms.ClientForm(instance=obj)
    form1=forms.ClientUserForm(instance=obj2)
    mydict={'form1':form1,'form2':form2}
    if request.method == 'POST':
        form1 = forms.ClientForm(data=request.POST, instance=obj)
        form2 = forms.ClientUserForm(data=request.POST, instance=obj)
        if form1.is_valid() and form2.is_valid():
            obj1 = form1.save(commit=False)
            obj2 = form2.save(commit=False)
            obj1.save()
            obj2.save()
            return render(request,'library/Clientupdated.html')
    return render(request,'library/updateclient.html',context=mydict)



def afterlogin_view(request):
    if is_admin(request.user):
        return render(request,'library/adminafterlogin.html')
    else:
        return render(request,'library/Clientafterlogin.html')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def addbook_view(request):
    form=forms.BookForm()
    if request.method=='POST':
        form=forms.BookForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'library/bookadded.html')
    return render(request,'library/addbook.html',{'form':form})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def BookUpdate(request, pk):
    obj = Book.objects.get(id=pk)
    form = forms.BookForm(instance=obj)
    if request.method == 'POST':
        form = forms.BookForm(data=request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return render(request,'library/bookupdated.html')
    return render(request,'library/updatebook.html',{'form':form})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def BookDelete(request, pk):
    obj = get_object_or_404(Book, pk=pk)

    obj.delete()
    books = models.Book.objects.all()
    return render(request, 'library/viewbook.html',{'books':books})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def ClientDelete(request, pk):
    obj = get_object_or_404(Client, pk=pk)
    obj.delete()
    Clients = models.Client.objects.all()
    return render(request, 'library/viewClient.html', {'Client': Clients})

#@login_required(login_url='adminlogin')
#@user_passes_test(is_admin)
#def Bookreturn(request, pk):
 #   obj = IssuedBook.objects.get(id=pk)
  #  obj.delete()
   # return render(request, 'library/viewissuedbook.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def viewClient_view(request):
    Client=models.Client.objects.all()
    return render(request,'library/viewClient.html',{'Client':Client})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def viewbook_view(request):
    books=models.Book.objects.all()
    return render(request,'library/viewbook.html',{'books':books})

@login_required(login_url='Clientlogin')
def viewbookbyClient_view(request):
    books=models.Book.objects.all()
    return render(request,'library/viewBookbyClient.html',{'books':books})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def issuebook_view(request ):
    form=forms.IssuedBookForm()
    if request.method=='POST':
        form=forms.IssuedBookForm(request.POST)
        if form.is_valid():
            if (Book.objects.get(isbn=request.POST.get('isbn2')).nb_exemplaire) >0:
                obj=models.IssuedBook()
                obj.idClient=request.POST.get('idClient2')
                obj.isbn=request.POST.get('isbn2')
                obj.save()
                book_pk = obj.isbn
                book = Book.objects.get(isbn=book_pk)
                book.nb_exemplaire = book.nb_exemplaire - 1
                book.save()
                return render(request,'library/bookissued.html')
            else :
                return render(request,'library/booknotissued.html')
    return render(request,'library/issuebook.html',{'form':form})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def viewissuedbook_view(request):
    issuedbooks=models.IssuedBook.objects.all()
    li=[]
    for ib in issuedbooks:
        issdate=str(ib.issuedate.day)+'-'+str(ib.issuedate.month)+'-'+str(ib.issuedate.year)
        expdate=str(ib.expirydate.day)+'-'+str(ib.expirydate.month)+'-'+str(ib.expirydate.year)
        #fine calculation
        days=(date.today()-ib.issuedate)
        print(date.today())
        d=days.days
        fine=0
        if d>15:
            day=d-15
            fine=day*10
        books=list(models.Book.objects.filter(isbn=ib.isbn))
        Client=list(models.Client.objects.filter(idClient=ib.idClient))
        i=0
        for l in books:
            t=(Client[i].idClient,books[i].isbn,issdate,expdate)
            i=i+1
            li.append(t)
    return render(request,'library/viewissuedbook.html',{'li':li})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def Return(request, pk):
    obj = IssuedBook.objects.get(isbn=pk)
    obj.delete()
    #obj = get_object_or_404(Client, issue=pk)
    #obj.delete()
    issuedbooks=models.IssuedBook.objects.all()
    return render(request, 'library/bookreturned.html')



@login_required(login_url='Clientlogin')
def ClientUpdatebyClient(request):
        obj2 = User.objects.filter(id=request.user.id).first()
        obj = models.Client.objects.filter(user_id=request.user.id).first()

        form2 = forms.ClientForm(instance=obj)
        form1=forms.ClientUserForm(instance=obj2)
        mydict={'form1':form1,'form2':form2}
        if request.method == 'POST':
            form1 = forms.ClientForm(data=request.POST, instance=obj)
            form2 = forms.ClientUserForm(data=request.POST, instance=obj)
            if form1.is_valid() and form2.is_valid():
                obj1 = form1.save(commit=False)
                obj2 = form2.save(commit=False)
                obj1.save()
                obj2.save()
                return render(request,'library/Clientafterlogin.html')
        return render(request,'library/updateclientb.html',context=mydict)






@login_required(login_url='Clientlogin')
def viewissuedbookbyClient(request):
    Client = models.Client.objects.filter(user_id=request.user.id)
    issuedbook = models.IssuedBook.objects.filter(idClient=Client[0].idClient)
    li1=[]
    li2=[]
    for ib in issuedbook:
        books=models.Book.objects.filter(isbn=ib.isbn)
        for book in books:
            t=(request.user,Client[0].idClient, book.name, book.author)
            li1.append(t)
        issdate=str(ib.issuedate.day)+'-'+str(ib.issuedate.month)+'-'+str(ib.issuedate.year)
        expdate=str(ib.expirydate.day)+'-'+str(ib.expirydate.month)+'-'+str(ib.expirydate.year)
        days=(date.today()-ib.issuedate)
        print(date.today())
        d=days.days
        fine=0
        if d>15:
            day=d-15
            fine=day*10
        t=(issdate,expdate)
        li2.append(t)
    contexe={'li1':li1,'li2':li2}
    return render(request,'library/viewissuedbookbyClient.html',contexe)


def aboutus_view(request):
    return render(request,'library/aboutus.html')

def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message, EMAIL_HOST_USER, ['wapka1503@gmail.com'], fail_silently = False)
            return render(request, 'library/contactussuccess.html')
    return render(request, 'library/contactus.html', {'form':sub})



def search_b(request):
        query = request.GET.get('q')
        if query  != '':
            results = Book.objects.filter(name__icontains=query)
        else:
            results = Book.objects.all()
        context = {
            'results': results,
        }
        return render(request, 'library/searchbook.html', context)


def search_bby(request):
    query = request.GET.get('q')
    if query != '':
        results = Book.objects.filter(name__icontains=query)
    else:
        results = Book.objects.all()
    context = {
        'results': results,
    }
    return render(request, 'library/searchbookby.html', context)


def search_c(request):
    query = request.GET.get('q')
    if query != '':
        results = Client.objects.filter(idClient__icontains=query)
    else:
        results = Client.objects.all()
    context = {
        'results': results,
    }
    return render(request, 'library/searchclient.html', context)