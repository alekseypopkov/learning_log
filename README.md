## Мы напишем веб-приложение «Журнал обучения»

- Создайте для проекта новый каталог learning_log, перейдите в этот каталог
в терминальном режиме и создайте виртуальную среду, используя следующие
команды:
```bash
learning_log$ python -m venv ll_env
```

```bash
source ll_env/bin/activate
```

- Запустить локальный сервер, выполнив команду: 
```bash
python manage.py runserver
```

models.py
from django.db import models

- Полный список всех полей, которые могут использоваться в модели, приведен в до-
кументе Django Model Field Reference на сайте https://docs.djangoproject.com/en/4.1/
ref/models/fields. Возможно, вся эта информация вам сейчас не понадобится, но она
будет в высшей степени полезной, когда вы начнете разрабатывать собственные
приложения.

- Каждый раз, когда вы захотите изменить данные, которыми управляет приложение
«Журнал обучения», выполните эти три действия: внесите изменения в models.py,
вызовите makemigrations для learning_logs и дайте Django указание выполнить
миграцию проекта (migrate).

```bash
python manage.py makemigrations learning_logs
```
```bash
python manage.py migrate
```
