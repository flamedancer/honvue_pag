# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from . import configs
from django.http import Http404


def index(request):
    return home(request)


def home(request):
    context = {'games': configs.GAMES, 'toptag': 'home'}
    return render(request, 'home.html', context)

def games(request, pag=1):
    gap = 3
    pag = int(pag)
    games = configs.GAMES[(pag -1)*gap:gap*pag]
    total_pags = range(1, ((len(configs.GAMES) - 1) / gap + 2))
    pre_pag = (pag - 1) if pag > 1 else 1
    next_pag = (pag + 1) if pag < total_pags[-1] else total_pags[-1]
    context = {'toptag': 'games', 'games': games, 'pag': pag, 'total_pags': total_pags, 'pre_pag': pre_pag, 'next_pag': next_pag}
    return render(request, 'games.html', context)

def news(request, pag=1):
    gap = 3 
    pag = int(pag)
    news = configs.NEWS[(pag -1)*gap:gap*pag]
    total_pags = range(1, ((len(configs.NEWS) - 1) / gap + 2))
    pre_pag = (pag - 1) if pag > 1 else 1
    next_pag = (pag + 1) if pag < total_pags[-1] else total_pags[-1]
    context = {'toptag': 'news', 'news': news, 'pag': pag, 'total_pags': total_pags, 'pre_pag': pre_pag, 'next_pag': next_pag}

    return render(request, 'news.html', context)

def business(request):
    context = {'toptag': 'business'}
    return render(request, 'business.html', context)

def joinUs(request):
    context = {'toptag': 'joinUs', 'jobs': configs.JOBS}
    return render(request, 'joinUs.html', context)

def aboutUs(request):
    context = {'toptag': 'aboutUs'}
    return render(request, 'aboutUs.html', context)

def gameDetail(request, game_index):
    game_index = int(game_index) 
    try:
        game = configs.GAMES[game_index]
    except IndexError:
        raise Http404("Game does not exist")
    context = {'game': game}
    return render(request, 'gameDetail.html', context)

def newsDetail(request, new_index):
    new_index = int(new_index) 
    try:
        new = configs.NEWS[new_index]
    except IndexError:
        raise Http404("Game does not exist")
    context = {'new': new}
    return render(request, 'newsDetail.html', context)

def jobDesc(request, category_index, job_index):
    category_index = int(category_index) 
    try:
        category = configs.JOBS[category_index]
    except IndexError:
        raise Http404("Job does not exist")

    job_index = int(job_index) 
    try:
        job = category['info'][job_index]
    except IndexError:
        raise Http404("Job does not exist")
    return HttpResponse(job['desc'].lstrip())
