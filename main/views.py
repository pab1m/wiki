import os

from django.core.exceptions import PermissionDenied
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Authors
from .models import About
from .forms import AuthorsForm
from .forms import AuthUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def index(request):
    if request.method == 'GET':
        authors = Authors.objects.order_by('-id')
        return render(request, 'index.html', {'title': "Головна сторінка", 'authors': authors})

@login_required(login_url="login")
def about(request):
    abouts = About.objects.all()
    return render(request, 'about.html', {'title': "Про нас", 'abouts': abouts})

@login_required(login_url="login")
def create(request):

    if request.method == 'POST':
        form = AuthorsForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            print(request.user.id)
            post.user_id = request.user.id
            post.save()
            return redirect('home')

    form = AuthorsForm()
    return render(request, 'create.html', {'form': form})


    # if request.method == 'POST':
    #     form = AuthorsForm(request.POST, request.FILES)
    #
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.user = request.user
    #         print(request.user)
    #         return redirect('home')
    #
    # form = AuthorsForm()
    # context = {
    #     'title': "Додавання автора",
    #     'form': form,
    # }
    #
    # return render(request, 'create.html', context)

@login_required(login_url="login")
def delete(request, pk):

    post = get_object_or_404(Authors, pk=pk)
    if post.user_id != request.user.id:
        return JsonResponse({'message': 'You are not the author of this post'})

    if post.photo:
        try:
            os.remove(post.photo.path)
        except Exception as e:
            print('Exception in removing profile image: ', e)
    post.delete()
    return redirect(reverse('home'))



    # get_authors = Authors.objects.get(pk=pk)
    # if get_authors.photo:
    #     try:
    #         os.remove(get_authors.photo.path)
    #     except Exception as e:
    #         print('Exception in removing profile image: ', e)
    # get_authors.delete()
    # return redirect(reverse('home'))

@login_required(login_url="login")
def update(request, pk):
    author = get_object_or_404(Authors, pk=pk)

    if author.user_id != request.user.id:
        return JsonResponse({'message': 'You are not the author of this post'})

    if request.method == 'POST':
        form = AuthorsForm(request.POST, instance=author)

        if form.is_valid():
            old_photo_path = author.photo.path

            form.save()

            if request.FILES.get('photo', None) is not None:
                try:
                    os.remove(old_photo_path)
                except Exception as e:
                    print('Exception in removing old profile image:', e)

                author.photo = request.FILES['photo']
                author.save()

            return redirect('home')
    else:
        form = AuthorsForm(instance=author)

    context = {
        'form': form,
        'update': True,
    }
    return render(request, 'update.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        users = User.objects.all()
        print(users)

        # if password == password2:
        user = authenticate(request, username=username, password=password)
        # if User.objects.filter(username=username).exists():
        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.info(request, "Дані введено некоректно")

    context = {
        'title': "Авторизація",
    }

    return render(request, 'login.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        users = User.objects.all()
        print(users)

        if password == password2:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('login')

    context = {
        'title': "Реєстрація",
    }

    return render(request, 'register.html', context)

def exit_user(request):
    logout(request)
    return redirect('home')


# def update(request, pk):
#     get_authors = Authors.objects.get(pk=pk)
#
#     if request.method == 'POST':
#         form = AuthorsForm(request.POST, instance=get_authors)
#
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#
#     context = {
#         'get_article': get_authors,
#         'update': True,
#         'form': AuthorsForm(instance=get_authors),
#     }
#     return render(request, 'update.html', context)
#
