# Cafe Order Management

## Описание проекта

**Cafe Order Management** — это веб-приложение для автоматизации процесса управления заказами в кафе. Приложение позволяет пользователям эффективно организовывать заказы, управлять меню и отслеживать статус каждого заказа.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/cybermizdav26/Cafe_Order_Management.git
2. Перейдите в директорию проекта:
    ```bash
    cd cafe-order-management
3. Установите необходимые библиотеки:
    ```bash
    pip install -r requirements.txt
4. Создайте и примените миграции базы данных и создать администратора:
    ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser

5. Запустите приложение
    ```bash
    python manage.py runserver

## Использование
1. Добавление заказа
Через веб-интерфейс пользователь вводит номер стола и список блюд с ценами.
Система автоматически добавляет заказ с уникальным ID, рассчитанной стоимостью и статусом “в ожидании”.
2. Удаление заказа
Пользователь через веб-интерфейс выбирает заказ по ID и удаляет его из системы.
3. Поиск заказа
Возможность поиска заказов по номеру стола или статусу через поисковую строку.
4. Отображение всех заказов
Веб-страница с таблицей всех заказов, отображающая их ID, номер стола, список блюд, общую стоимость и статус.
5. Изменение статуса заказа
Пользователь через интерфейс выбирает заказ по ID и изменяет его статус (“в ожидании”, “готово”, “оплачено”).
6. Расчет выручки за смену
Отдельная страница или модуль для расчета общего объема выручки за заказы со статусом “оплачено”.

## API в DRF
Для просмотра документации API перейдите по адресу:
````
   127.0.0.1/swagger/
````
Здесь все маршруты
```
   - /orders/ — отображение списка заказов (OrderListAPIView).
   - /menu-create/ — создание новых блюд меню (MenuCreateApiView).
   - /menu/ — список всех блюд меню (MenuListApiView).
   - /order-create/ — создание нового заказа (OrderCreateAPIView).
   - /order-delete<int:pk> — удаление заказа (OrderDeleteAPIView).
   - /order-update<int:pk> — обновление статуса заказа (OrderUpdateApiView).
   - /revenue/ — получение общей выручки (RevenueAPIView).
   - /orders-search/ — поиск заказов с фильтрацией (OrderSearchAPIView).
```
## Docker
   ```bash
   docker-compose up -p
   docker-compose exec web pip install -r requirements.txt
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py runserver
```
   
## Конфигурация
Для настройки приложения используйте файлы конфигурации в директории /config.

## Вклад
Для внесения вклада в проект создавайте пулл-реквесты или сообщайте об ошибках через GitHub Issues.


## Связь
Для вопросов и предложений вы можете связаться со мной через:
    
    GitHub: cybermizdav26 
    Email: cybermizrobov72022@gmail.com
