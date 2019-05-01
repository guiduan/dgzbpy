from django.shortcuts import render
from auth.models import models


def register(request):
    return render(request, 'auth/register.html', {'title': 'this is my auth/register title', 'message': 'this is my auth/register page'})

def login(request):
    return render(request,'auth/login.html',{'title':'this is my auth/login title', 'message': 'this is my auth/login page'})
