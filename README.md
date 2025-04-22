## Мы напишем веб-приложение «Журнал обучения»

### Активация виртуальной среды
- Создайте для проекта новый каталог learning_log, перейдите в этот каталог
в терминальном режиме и создайте виртуальную среду, используя следующие
команды:
learning_log$ python -m venv ll_env
learning_log$

```bash
learning_log$ python -m venv ll_env
```

```bash
source ll_env/bin/activate
```

Чтобы завершить использование виртуальной среды, введите команду deactivate:
(ll_env)learning_log$ deactivate
learning_log$

```bash
deactivate
```

### Установка Django

- После того как вы создали свою виртуальную среду и активизировали ее, устано-
вите Django с помощью инструмента pip:
(ll_env)learning_log$ pip install --upgrade pip
(ll_env)learning_log$ pip install django

```bash
pip install --upgrade pip
```
```bash
pip install django
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
