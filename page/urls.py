from django.urls import path
from .views import(
    about_us_view,
    contact_view,
    home_view,
)

urlpatterns = [
    path("",home_view, name="home"),
    path("hakkimizda/", about_us_view, name="about_us"),
    path("iletisim/", contact_view, name="contact"),
]