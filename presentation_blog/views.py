from django.shortcuts import render
import os

from kosar_website.settings import BASE_DIR


def show_index(request):
    return render(request, "presentation_blog/index.html")