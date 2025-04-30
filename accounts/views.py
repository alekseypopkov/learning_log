from django.shortcuts import render

# Create your views here.

def index(request):
    """Главная страница приложения "Журнал обучения"."""
    return render(request, 'index.html')
