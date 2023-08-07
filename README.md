# Проект "Торговая сеть"

Этот проект представляет собой веб-приложение для управления торговой сетью. Оно позволяет пользователям просматривать, 
добавлять, обновлять и удалять информацию о продуктах, категориях, а также управлять корзиной покупок.

## Стек технологий

- Python 3.10
- Django 3.2.6
- PostgreSQL
- Django REST framework
- Docker (опционально)
- Git

## Установка и настройка

1. Склонируйте репозиторий на свой локальный компьютер:

   ```bash
   git clone https://github.com/username/trading_network.git
   cd trading_network
Создайте и активируйте виртуальное окружение:


Copy code
python -m venv myenv
source myenv/bin/activate  # для Windows: myenv\Scripts\activate
Установите зависимости из файла requirements.txt:

Copy code
pip install -r requirements.txt
Настройте переменные окружения в файле .env:

env
Copy code
SECRET_KEY=""
DEBUG=True
ALLOWED_HOSTS=['localhost', '127.0.0.1']

POSTGRES_PASSWORD=""
POSTGRES_USER=""
POSTGRES_DB=""
DB_PORT=5432
POSTGRES_HOST=postgres

Примените миграции базы данных:

Copy code
python manage.py migrate
Создайте суперпользователя для доступа к административной панели:

python manage.py createsuperuser
Запустите сервер разработки:

python manage.py runserver
Приложение будет доступно по адресу http://localhost:8000/.

Использование
После установки и настройки вы можете использовать веб-приложение для управления торговой сетью. 
Вы можете войти в административную панель с помощью суперпользователя, созданного на шаге 6. Затем вы можете добавлять, 
обновлять и удалять информацию о продуктах, категориях, а также просматривать корзину покупок.