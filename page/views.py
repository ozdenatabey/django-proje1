from django.shortcuts import render
from django.http import HttpResponse
from random import randint


FAKE_DB_PROJECTS = [
    f"https://picsum.photos/id/{id}/120/80" for id in range(21,29)
]

FAKE_DB_CAROUSEL = [
    f"https://picsum.photos/id/{id}/1200/250" for id in range(50,54)
]

def home_view(request):
    # context = {"platform": f"Django platformu kullanıldı ve randint ile dönen veri:{randint(1,100)}"}
    page_title = ("Ana Sayfa")
    context = dict(
        page_title = page_title,
        FAKE_DB_PROJECTS = FAKE_DB_PROJECTS,
        FAKE_DB_CAROUSEL = FAKE_DB_CAROUSEL,
    )
    return render(request, "page/index.html", context)

def about_us_view(request):
    page_title = ("Hakkımızda")
    context = dict(
        page_title = page_title,
        FAKE_DB_PROJECTS = FAKE_DB_PROJECTS,
    )
    return render(request, "page/hakkimizda.html", context)

def contact_view(request):
    page_title = ("İletişim")
    context = dict(
        page_title = page_title,
        FAKE_DB_PROJECTS = FAKE_DB_PROJECTS,
    )
    return render(request, "page/iletisim.html", context)
