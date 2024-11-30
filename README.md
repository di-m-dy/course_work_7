# «Атомные привычки»
## бэкенд-часть SPA веб-приложения

![pic](cover.png)

### Описание
Проект представляет собой бэкенд-часть SPA веб-приложения, которое позволяет пользователям создавать и редактировать свои привычки. 
Привычки могут быть как ежедневными, так и еженедельными. 

### Функционал
- Регистрация и авторизация пользователей
- Создание, редактирование и удаление привычек
- Просмотр списка всех привычек пользователя
- Просмотр списка публичных привычек всех пользователей
- Оповещение пользователя о выполнении привычки в Telegram

### Requirements

* celery==5.4.0
* coverage==7.6.8
* Django==5.1.2
* django-celery-beat==2.7.0
* django-filter==24.3
* django-phone-field==1.8.1
* django-timezone-field==7.0
* djangorestframework==3.15.2
* djangorestframework-simplejwt==5.3.1
* drf-yasg==1.21.8
* pillow==11.0.0
* psycopg2-binary==2.9.10
* PyJWT==2.10.1
* python-dotenv==1.0.1
* pytz==2024.2
* redis==5.2.0
* requests==2.32.3


### Установка
1. Клонируйте репозиторий 

2. Создайте виртуальное окружение
```shell 
python -m venv venv
```
3. Установите зависимости из файла requirements.txt
```shell
pip install -r requirements.txt
```
4. Скоипруйте файл env_template в .env и укажите свои переменные окружения
5. Выполните миграции
```shell
python manage.py migrate
```
6. Запустите redis-server
```shell
redis-server
```
7. Запустите celery worker и celery beat
```shell
celery -A config worker -l info
celery -A config beat -l info
```
8. Запустите сервер
```shell
python manage.py runserver
```

### Документация
Документация доступна по адресу http://localhost:8000/redoc/
