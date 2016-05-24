# -*- coding: utf-8 -*-
from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'home.html', context)


def home(request):
    context = {}
    return render(request, 'home.html', context)

def games(request):
    context = {}
    return render(request, 'games.html', context)

def news(request):
    context = {}
    return render(request, 'news.html', context)

def business(request):
    context = {}
    return render(request, 'business.html', context)

def joinUs(request):
    context = {}
    return render(request, 'joinUs.html', context)

def aboutUs(request):
    context = {}
    return render(request, 'aboutUs.html', context)

def gameDetail(request):
    context = {}
    return render(request, 'gameDetail.html', context)
