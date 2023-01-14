from django.shortcuts import render
from django.http import HttpResponse
from random import randint


def home_view(request):
    # context = {"platform": f"Django platformu kullanıldı ve randint ile dönen veri:{randint(1,100)}"}
    context = dict()
    return render(request, "page/index.html", context)

def about_us_view(request):
    context = dict()
    return render(request, "page/hakkimizda.html", context)

def contact_view(request):
    context = dict()
    return render(request, "page/iletisim.html", context)
