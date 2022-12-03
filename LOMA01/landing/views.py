from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
def index(request):
    # if request.user.is_authenticated:
    return render(request, "landing/index.html")


def landing_page(request):
    # if request.user.is_authenticated:
    return render(request, "landing/landing_page.html")

def er404(request):
    return HttpResponse("<h1>Страница не найдено. Код ошибки 404</h1><a href='/'>Home</a>")
