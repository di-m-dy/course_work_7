# Описание задач
Добавьте необходимые модели привычек.
Реализуйте эндпоинты для работы с фронтендом.
Создайте приложение для работы с Telegram и рассылками напоминаний.

# Модели
В книге хороший пример привычки описывается как конкретное действие, которое можно уложить в одно предложение:

я буду `[ДЕЙСТВИЕ]` в `[ВРЕМЯ]` в `[МЕСТО]`

За каждую полезную привычку необходимо себя вознаграждать или сразу после делать приятную привычку. 
Но при этом привычка не должна расходовать на выполнение больше двух минут. 
Исходя из этого получаем первую модель — «Привычка».

## Привычка:

* Пользователь — создатель привычки.
* Место — место, в котором необходимо выполнять привычку.
* Время — время, когда необходимо выполнять привычку.
* Действие — действие, которое представляет собой привычка.
* Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки.
* Связанная привычка — привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных.
* Периодичность (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях.
* Вознаграждение — чем пользователь должен себя вознаградить после выполнения.
* Время на выполнение — время, которое предположительно потратит пользователь на выполнение привычки.
* Признак публичности — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки.

_Обратите внимание, что в проекте у вас может быть больше, чем одна описанная здесь модель._


# Валидаторы

* Исключить одновременный выбор связанной привычки и указания вознаграждения.

_В модели не должно быть заполнено одновременно и поле вознаграждения, и поле связанной привычки._ 
_Можно заполнить только одно из двух полей._

* Время выполнения должно быть не больше 120 секунд.
* В связанные привычки могут попадать только привычки с признаком приятной привычки.
* У приятной привычки не может быть вознаграждения или связанной привычки.
* Нельзя выполнять привычку реже, чем 1 раз в 7 дней.

_Нельзя не выполнять привычку более 7 дней. Например, привычка может повторяться раз в неделю,_ 
_но не раз в 2 недели. За одну неделю необходимо выполнить привычку хотя бы один раз._

# Пагинация

Для вывода списка привычек реализовать пагинацию с выводом по 5 привычек на страницу.


# Права доступа

* Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD.
* Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять.

# Эндпоинты

* Регистрация.
* Авторизация.
* Список привычек текущего пользователя с пагинацией.
* Список публичных привычек.
* Создание привычки.
* Редактирование привычки.
* Удаление привычки.

# Интеграция
Для полноценной работы сервиса необходимо реализовать работу с отложенными задачами для напоминания о том, 
в какое время какие привычки необходимо выполнять.

Для этого потребуется интегрировать сервис с мессенджером Телеграм, 
который будет заниматься рассылкой уведомлений.

# Безопасность
Для проекта необходимо настроить CORS, чтобы фронтенд мог подключаться к проекту на развернутом сервере.

# Документация
Для реализации экранов силами фронтенд-разработчиков необходимо настроить вывод документации. 
При необходимости эндпоинты, на которые документация не будет сгенерирована автоматически, описать вручную.

# Критерии приемки курсовой работы
* Настроили CORS.
* Настроили интеграцию с Телеграмом.
* Реализовали пагинацию.
* Использовали переменные окружения.
* Все необходимые модели описаны или переопределены.
* Все необходимые эндпоинты реализовали.
* Настроили все необходимые валидаторы.
* Описанные права доступа заложены.
* Настроили отложенную задачу через Celery.
* Проект покрыли тестами как минимум на 80%.
* Код оформили в соответствии с лучшими практиками.
* Имеется список зависимостей.
* Результат проверки Flake8 равен 100%, при исключении миграций.
* Решение выложили на GitHub.