# -*- coding: utf-8 -*-
from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'home_pag.html', context)


