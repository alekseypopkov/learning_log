from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """Тема, которую изучает пользователь."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Темы'
        verbose_name_plural = 'Темы'

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.text


class Entry(models.Model):
    """Информация, изученная пользователем по теме."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Записи'
        verbose_name_plural = 'Записи'
        
    def __str__(self):
        """Возвращает строковое представление модели."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text}"