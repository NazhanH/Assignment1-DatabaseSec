from django.shortcuts import render,  redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.contrib.auth.models import Group

from django.contrib import messages

from .forms import CreateUserForm

from .decoraters import unauthenticated_user, allowed_users, admin_only

from .models import *

from django.db.models import Count

# Create your views here.
def home(request, *args, **kwargs):
    

    context = {
        
    }
    return render(request, 'home.html', context)


def catalogue(request):
    book_titles = Book.objects.values('title').annotate(title_count=Count('title')).filter(title_count__gte=1)
    books = [Book.objects.filter(title=book['title']).first() for book in book_titles]
    context = {
        'books': books,
    }
    return render(request, 'catalogue.html', context)

@unauthenticated_user
def register(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='Patrons')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)
            
            

            auth_login(request, user)
            return redirect('home')
        
    context = {'form': form}
    return render(request, 'register.html', context)

@unauthenticated_user
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('home')
