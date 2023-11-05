# # For more information, please refer to https://aka.ms/vscode-docker-python
# FROM python:3.10-slim

# EXPOSE 8000

# # Keeps Python from generating .pyc files in the container
# ENV PYTHONDONTWRITEBYTECODE=1

# # Turns off buffering for easier container logging
# ENV PYTHONUNBUFFERED=1

# # Install pip requirements
# COPY requirements.txt .
# RUN python -m pip install -r requirements.txt

# WORKDIR /app
# COPY . /app

# # Creates a non-root user with an explicit UID and adds permission to access the /app folder
# # For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
# RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
# USER appuser

# # During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "InfoAccounting.wsgi"]

# Указываем базовый образ, основанный на Python
FROM python:3.9

# Устанавливаем переменную окружения PYTHONUNBUFFERED в значение 1
# Это гарантирует, что вывод Python будет отправляться прямо в терминал без буферизации
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы requirements.txt в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости, перечисленные в файле requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . /app/

# Запускаем команду для выполнения миграций Django и сбора статических файлов
RUN python manage.py migrate
# RUN python manage.py collectstatic --noinput

# Открываем порт, который будет использоваться вашим Django приложением
EXPOSE 8000

# Запускаем сервер Django при старте контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
