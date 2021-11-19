from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'mainapp/index.html')  #Второй параметр - это путь html страницы, относительно templates