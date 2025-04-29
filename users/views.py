from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm

# Create your views here.

def new_topic(request):
    """Добавляет новую тему."""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = TopicForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)