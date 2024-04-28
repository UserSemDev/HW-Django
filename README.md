### Интернет магазин на фреймворке Django

### Описание проекта:

##### Технологии:
- Python
- Django
- python-dotenv
- psycopg2-binary
- pillow
- ipython
- pytils

#### Инструкция для запуска проекта:
- Клонировать проект
- Создать и активировать виртуального окружения
- Установить зависимости
- Создать файл .env
- Запустить проект


##### Клонирование проекта:
- git clone https://github.com/UserSemDev/HW-Django.git

##### Настройка виртуального окружение и установка зависимостей:
- [Инструкция по установке](https://sky.pro/media/kak-sozdat-virtualnoe-okruzhenie-python/)

##### Создание файла .env

- В корне проекта создайте файл .env со следующими параметрами
    ``` ini
    ENGINE="postgresql_psycopg2"
    NAME="db_name" - название вашей БД
    PGUSER="postgres" - имя пользователя БД
    PASSWORD="secret" - пароль пользователя БД
    HOST="host" - можно указать "localhost" или "127.0.0.1"
    PORT=port - указываете порт для подключения по умолчанию 5432

    EMAIL_HOST_USER='your_email@yandex.ru' - ваш email yandex
    EMAIL_HOST_PASSWORD='your_yandex_smtp_password' - ваш пароль smtp (подробнее о настройке ниже)
    EMAIL_HOST_TO_USER='recipient@example.com' - email получателя сообщений
    ```
- О настройке почты smtp: 
[Настройка почтового сервиса SMTP ](https://proghunter.ru/articles/setting-up-the-smtp-mail-service-for-yandex-in-django)

##### Запуск проекта:
- примените миграции:
  ```text
  python manage.py migrate
  ```
- примените фикстуры:
  ```text
  python -Xutf8 manage.py loaddata fixtures/*.json
  ```
- запустите проект и перейтиде по адресу:
  ```text
  python manage.py runserver
  ```