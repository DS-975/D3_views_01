# region todo: Создаём виртуальное окружение (venv)
# python -m venv venv
# todo: Активируем виртуальное окружение
# .\venv\Scripts\activate
# endregion

# region todo: Устанавливаем библиотеку Django
# pip install django
# endregion

# region todo: Запуски сервера
# python manage.py runserver
# endregion

# region todo: Создаём новые миграции
# python manage.py makemigrations
# endregion

# region todo: Применяем миграции
# python manage.py migrate
# endregion

# region todo: Создание админки
# todo: Применяем миграции
# python manage.py migrate
# todo: в Terminal пишем команду
# python manage.py createsuperuser
# | Username: admin |
# | Password: admin |
# todo: Запуски сервера
# python manage.py runserver
# endregion

# region # todo: Создал новый Django-проект
# django-admin startproject project
# endregion

# region # todo: Создал приложение news
# todo: Переходим в папку project
# cd .\project
# todo: Создал приложение news
# python manage.py startapp news
# endregion

# region todo: Установка и настройка приложение Flatpages | Документация - > https://docs.djangoproject.com/en/3.1/ref/contrib/flatpages/
# todo: [ 1 ] В project/project/settings.py -> INSTALLED_APPS | 29 | 'django.contrib.sites', # <- Для работы приложения Flatpages
#                                                             | 30 | 'django.contrib.flatpages', # <- Для работы приложения Flatpages
#
# todo: [ 2 ] В project/project/settings.py -> MIDDLEWARE | 41 | 'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware', # <- Для работы приложения Flatpages
#
# todo: [ 3 ] В project/project/settings.py -> | 44 | SITE_ID = 1 # <- Для работы приложения Flatpages
#
# todo: [ 4 ] В project/project/settings.py -> |  2 | import os # <- импортируем os для работы приложения Flatpages
#                                              | 51 | 'DIRS': [os.path.join(BASE_DIR, 'templates')], # <- Для работы приложения Flatpages
#
# todo: [ 5 ] В project/project/urls.py -> | include | 2 | from django.urls import path, include # include <- Для работы приложения Flatpages
#
# todo: [ 6 ] В project/project/urls.py -> | 6 | path('pages/', include('django.contrib.flatpages.urls')), # <- Для работы приложения Flatpages
#
# todo: [ 7 ] В project -> New -> File -> templates/flatpages/default.html
# endregion

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# ↓ + ↓ B project/news/models.py
# |  1 | from django.db import models
# |  2 | from django.core.validators import MinValueValidator
# |  3 |
# |  4 |
# |  5 | # Товар для нашей витрины
# |  6 | class Product(models.Model):
# |  7 | name = models.CharField(
# |  8 | max_length=50,
# |  9 | unique=True, # названия товаров не должны повторяться
# | 10 |    )
# | 11 | description = models.TextField()
# | 12 | quantity = models.IntegerField(
# | 13 | validators=[MinValueValidator(0)],
# | 14 |    )
# | 15 | # поле категории будет ссылаться на модель категории
# | 16 | category = models.ForeignKey(
# | 17 | to='Category',
# | 18 | on_delete=models.CASCADE,
# | 19 | related_name='products', # все продукты в категории будут доступны через поле products
# | 20 |    )
# | 21 | price = models.FloatField(
# | 22 | validators=[MinValueValidator(0.0)],
# | 23 |    )
# | 24 |
# | 25 | def __str__(self):
# | 26 | return f'{self.name.title()}: {self.description[:20]}'
# | 27 |
# | 28 |
# | 29 | # Категория, к которой будет привязываться товар
# | 30 | class Category(models.Model):
# | 31 | # названия категорий тоже не должны повторяться
# | 32 | name = models.CharField(max_length=100, unique=True)
# | 33 |
# | 34 | def __str__(self):
# | 35 | return self.name.title()
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# ↓ + ↓ B project/news/admin.py
# | 1 | from django.contrib import admin
# | 2 | from .models import Category, Product
# | 3 |
# | 4 |
# | 5 | admin.site.register(Category)
# | 6 | admin.site.register(Product)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# ↓ + ↓ B project/news/views.py
# | 1 | # Импортируем класс, который говорит нам о том,
# | 2 | # что в этом представлении мы будем выводить список объектов из БД
# | 3 | from django.views.generic import ListView
# | 4 | from .models import Product
# | 5 |
# | 6 |
# | 7 | class ProductsList(ListView):
# | 8 |
# | 9 | # Указываем модель, объекты которой мы будем выводить
# | 10 | model = Product
# | 11 |
# | 12 | # Поле, которое будет использоваться для сортировки объектов
# | 13 | ordering = 'name'
# | 14 |
# | 15 | # Указываем имя шаблона, в котором будут все инструкции о том,
# | 16 | # как именно пользователю должны быть показаны наши объекты
# | 17 | template_name = 'products.html'
# | 18 |
# | 19 | # Это имя списка, в котором будут лежать все объекты.
# | 20 | # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
# | 21 | context_object_name = 'products'
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# B project/news -> New -> File -> urls.py
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# ↓ + ↓ B project/news/urls.py
# | 1 | from django.urls import path
# | 2 | # Импортируем созданное нами представление
# | 3 | from .views import ProductsList
# | 4 |
# | 5 |
# | 6 | urlpatterns = [
# | 7 | # path — означает путь.
# | 8 | # Т.к. наше объявленное представление является классом,
# | 9 | # а Django ожидает функцию, нам надо представить этот класс в виде view.
# | 10 | # Для этого вызываем метод as_view.
# | 11 | path('', ProductsList.as_view()),
# | 12 | ]
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# ↓ + ↓ B project/project/urls.py
# | 1 || 1 | from django.contrib import admin
# | 2 | from django.urls import path, include
# | 3 |
# | 4 | urlpatterns = [
# | 5 | path('admin/', admin.site.urls),
# | 6 | path('pages/', include('django.contrib.flatpages.urls')),
# | 7 |
# | 8 | # Делаем так, чтобы все адреса из нашего приложения (news/urls.py)
# | 9 | # подключались к главному приложению с префиксом products/.
# | 10 | path('products/', include('news.urls')),
# | 11 ] ]
#
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# B projec/templates -> New -> File -> products.html
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# B projec/templates/products.html -> | 1 | <!--  наследуемся от шаблона default.html, который мы создавали для flatpages -->
# | 2 | {% extends 'flatpages/default.html' %}
# | 3 |
# | 4 | <!-- Название у нас будет products -->
# | 5 | {% block title %}
# | 6 | Products
# | 7 | {% endblock title %}
# | 8 |
# | 9 | <!-- В контенте на странице мы выводим все товары -->
# | 10 | {% block content %}
# | 11 | <h1>Все товары</h1>
# | 12 | {{ products }}
# | 13 | {% endblock content %}
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
#
# Напомним, что скачать шаблон и статические файлы можно по ссылке.
# После скачивания нужно создать папку static
# и добавить в нее файлы styles.css
# по пути project/static/css/styles.css
# и index.html в project/static/index.html.
# В templates/flatpages/default.html должен быть
# базовый HTML темплейт.
# Вспомнить, что и как нужно настроить, вы можете в модуле D1.
#
# B projec -> New -> File -> static/css/styles.css
#
# B project/static -> New -> File -> index.html
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# Запускаем окно командной строки
# python manage.py shell
# from newapp.models import *
