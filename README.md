# Инструкция по запуску проекта

## 1. Клонировать репозиторий

```bash
git clone <url-репозитория>
cd test_task
```

## 2. Создать и активировать виртуальное окружение

### Linux / macOS
```bash
python -m venv venv
source venv/bin/activate
```

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

## 3. Установить зависимости

```bash
pip install -r requirements.txt
```

Если файла `requirements.txt` нет, установите зависимости вручную:

```bash
pip install django psycopg2-binary python-dateutil
```

## 4. Настроить базу данных PostgreSQL

Создайте базу данных и пользователя, например через `pgAdmin` или `psql`:

```sql
CREATE USER test_user WITH PASSWORD 'test123';
CREATE DATABASE test_task_db OWNER test_user;
GRANT ALL PRIVILEGES ON DATABASE test_task_db TO test_user;
```

В файле `test_task/settings.py` укажите параметры подключения:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test_task_db',
        'USER': 'test_user',
        'PASSWORD': 'test123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 5. Выполнить миграции

```bash
python manage.py makemigrations
python manage.py migrate
```

## 6. Загрузить тестовые данные

```bash
python manage.py load_test_data
```

Эта команда заполнит таблицы `Client` и `Payment` данными из задания.

---

Запуск сервера

```bash
python manage.py runserver
```

Откройте в браузере:

```text
http://127.0.0.1:8000/
```
