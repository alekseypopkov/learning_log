from django.shortcuts import render

# Create your views here.

def index(request):
    """Главная страница приложения "Сино-корейские числительные - KOREAN NUMERALS."""
    return render(request, 'sk_numerals_logs/index.html')
