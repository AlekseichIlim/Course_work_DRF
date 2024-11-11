FROM python:3.12

WORKDIR /app

# Копируем только файл с зависимостями
COPY /requirements.txt /

# Устанавливаем Poetry и зависимости
RUN pip install -r /requirements.txt --no-cache-dir

COPY . .

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver"]