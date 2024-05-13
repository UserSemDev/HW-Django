### Интернет магазин на фреймворке Django

### Описание проекта:


##### Технологии:
- Django
- python-dotenv
- psycopg2-binary
- pillow
- ipython
- pytils


#### Инструкция для запуска проекта:
1. Клонировать проект
2. Настроить виртуальное окружение
3. Отредактировать .env.sample
4. Настройка БД
5. Запустить проект


##### 1. Клонирование проекта:
- git clone https://github.com/UserSemDev/HW-Django.git

##### 2. Настройка виртуального окружение и установка зависимостей:

- Инструкция для работы через виртуальное окружение - poetry: 
```text
poetry init - Создает виртуальное окружение
poetry shell - Активирует виртуальное окружение
poetry install - Устанавливает зависимости
```

- Инструкция для работы через виртуальное окружение - pip:

Создает виртуальное окружение:
```text
python3 -m venv venv
```

Активирует виртуальное окружение:
```text
source venv/bin/activate          # для Linux и Mac
venv\Scripts\activate.bat         # для Windows
```

Устанавливает зависимости:
```
pip install -r requirements.txt
```


##### 3. Редактирование .env.sample:

- В корне проекта переименуйте файл .env.sample в .env и отредактируйте параметры:
    ```text
    ENGINE="postgresql_psycopg2"
    NAME="db_name" - название вашей БД
    PGUSER="postgres" - имя пользователя БД
    PASSWORD="secret" - пароль пользователя БД
    HOST="host" - можно указать "localhost" или "127.0.0.1"
    PORT=port - указываете порт для подключения по умолчанию 5432

    EMAIL_HOST_USER='your_email@yandex.ru' - ваш email yandex
    EMAIL_HOST_PASSWORD='your_yandex_smtp_password' - ваш пароль smtp (подробнее о настройке ниже)
    EMAIL_HOST_TO_USER='recipient@example.com' - email получателя сообщений
  
    ADMIN_EMAIL='admin@test.com' - email регистрации администратора сайта
    ADMIN_PASSWORD='secret' - пароль регистрации администратора сайта
  
    SECRET_KEY=secret_key - секретный ключ django проекта
    DEBUG=True - режим DEBUG
    REDIS_HOST=redis://host:port - данные местоположения redis
    CACHE_ENABLED=True - использование кэша
    ```
- О настройке почты smtp: 
[Настройка почтового сервиса SMTP ](https://proghunter.ru/articles/setting-up-the-smtp-mail-service-for-yandex-in-django)


##### 4. Настройка БД и кэширования:

- Примените миграции:
  ```text
  python manage.py migrate
  ```
  
- Примените фикстуры:
  ```text
  python manage.py loaddata fixtures/*.json
  ```
  
- Установите Redis:

  - Linux команда:
   ```text
   sudo apt install redis; или sudo yum install redis;
   ```

  - macOS команда:
   ```text
   brew install redis;
   ```

  Windows инструкция:
  - [Перейти на Redis docs](https://redis.io/docs/install/install-redis/install-redis-on-windows/)
    
##### 5. Запуск проекта:

- Запустите проект:

  ```text
  python manage.py runserver
  ```
- Перейдите по адресу:
  [http://127.0.0.1:8000](http://127.0.0.1:8000/)

  