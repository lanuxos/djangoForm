from django.shortcuts import render
# from django.http import HttpResponse

def Home(request):
    context = {}
    return render(request, 'form/home.html', context)

def Add(request):
    context = {}
    return render(request, 'form/add.html', context)