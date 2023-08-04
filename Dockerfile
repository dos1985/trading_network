# Базовый образ Python (в нем уже установлен Python, pip и прочее)
FROM python:3.10-slim
# Установка переменных окружения
ENV PYTHONUNBUFFERED 1
# Создаем директорию /treding и переходим в нее
WORKDIR /app
# Копируем файл с зависимостями
COPY requirements.txt .
# Устанавливаем через pip зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# Копируем код приложения
COPY . .
# Показываем содержимое /app
RUN ls -la /app
# Определение порта
EXPOSE 8000
# Указываем команду, которая будет запущена командой docker run
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]