from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

def home_page(request):
    context = {}
    return render(request, 'home.html', context)


def about_page(request):
    context = {}
    return render(request, 'about.html', context)