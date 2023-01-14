## Тестовое задание UpTrader На должность Junior Backend Developer
## Реализация древовидного меню с помощью templatetags

### Как работает:

Стек:
* Python 3.10
* Django 4.1.2


Создаем и активируем виртуальное окружение:

```
mkdir /opt/venv 
```
```
python3 -m venv /opt/venv/treemenu_env
```
```
source /opt/venv/treemenu_env/bin/activate
```
Устанавливаем Django 4.1.2:
```
pip3 install Django==4.1.2
```
#### Переходим в папку с проектом и создаем суперпользователя для доступа к панели администратора
```
python3 manage.py createsuperuser
```
Создаем миграции:
```
python3 manage.py makemigrations
```
Выполняем миграции:
```
python3 manage.py migrate
```
#### Запускаем сервер
```
python3 manage.py runserver
```
В панели администратора создаем меню и айтемы. Для вложенности, айтему вручную указывается родитель.
Рендер происходит на странице /menu
