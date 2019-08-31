# -*- coding: utf-8 -*-
"""
time:2019/8/30 21:30
"""

from django.shortcuts import render
from log.models import Log


def home(request):
    text_objs = Log.objects
    return render(request, "home.html", {"text_objs": text_objs})
