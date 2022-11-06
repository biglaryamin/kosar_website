from django.shortcuts import render, HttpResponse



def test(request):
    return render(request, "crawler/list.html")