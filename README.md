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

### Установка Docker на сервер (Ubuntu 20.04)
1. Установите необходимые пакеты
```shell
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```
2. Добавьте GPG ключ Docker
```shell
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```
3. Добавьте репозиторий Docker
```shell
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
4. Установите Docker
```shell
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io
```
5. Добавьте своего пользователя в группу docker
```shell
sudo usermod -aG docker $USER
```
6. Перезапустите Docker
```shell
sudo systemctl restart docker
```

### Установка проекта
1. Клонируйте репозиторий
2. Скопируйте файл env_template в .env и заполните своими данными

### Запуск проекта
1. Перейдите в папку проекта
2. Выполните команду
```shell
docker-compose up -d --build
```

### Документация
Документация доступна по адресу http://localhost:8000/redoc/
