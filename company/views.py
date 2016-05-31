# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from . import configs
from .models import Game, New, JobCategory, Job
from django.http import Http404
from django.shortcuts import get_object_or_404


def index(request):
    return home(request)


def home(request):
    games = Game.objects.order_by('index')
    context = {'games': games, 'toptag': 'home'}
    return render(request, 'home.html', context)

def games(request, pag=1):
    gap = 3
    pag = int(pag)
    all_games = Game.objects.order_by('index') 
    games = all_games[(pag -1)*gap:gap*pag]
    total_pags = range(1, ((len(all_games) - 1) // gap + 2))
    pre_pag = (pag - 1) if pag > 1 else 1
    next_pag = (pag + 1) if pag < total_pags[-1] else total_pags[-1]
    context = {'toptag': 'games', 'games': games, 'pag': pag, 'total_pags': total_pags, 'pre_pag': pre_pag, 'next_pag': next_pag}
    return render(request, 'games.html', context)

def news(request, pag=1):
    gap = 3 
    pag = int(pag)
    all_news = New.objects.order_by('-pub_date')
    news = all_news[(pag -1)*gap: gap*pag]
    total_pags = range(1, ((len(all_news) - 1) // gap + 2))
    pre_pag = (pag - 1) if pag > 1 else 1
    next_pag = (pag + 1) if pag < total_pags[-1] else total_pags[-1]
    context = {'toptag': 'news', 'news': news, 'pag': pag, 'total_pags': total_pags, 'pre_pag': pre_pag, 'next_pag': next_pag}

    return render(request, 'news.html', context)

def business(request):
    context = {'toptag': 'business'}
    return render(request, 'business.html', context)

def joinUs(request):
    categorys = JobCategory.objects.order_by('index')
    context = {'toptag': 'joinUs', 'categorys': categorys}
    return render(request, 'joinUs.html', context)

def aboutUs(request):
    context = {'toptag': 'aboutUs'}
    return render(request, 'aboutUs.html', context)

def gameDetail(request, game_index):
    game_index = int(game_index) 
    game = get_object_or_404(Game, index=game_index)
    context = {'toptag': 'games', 'game': game}
    return render(request, 'gameDetail.html', context)

def newsDetail(request, new_id):
    new_id = int(new_id) 
    new = get_object_or_404(New, id=new_id)
    context = {'toptag': 'news', 'new': new}
    return render(request, 'newsDetail.html', context)

def jobDesc(request, job_id):
    try:
        job = get_object_or_404(Job, id=job_id)
    except IndexError:
        raise Http404("Job does not exist")
    return HttpResponse(job.desc.lstrip())
