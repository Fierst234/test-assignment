# Тестовое задание Effective Mobile
## Запуск проекта
1. Клонирование репозитория
    ```bash 
    git clone https://github.com/Fierst234/test-assignment.git
    ```

2. Открытие директории и сборка
    ```bash 
    cd test-assignment && docker compose up -d
    ```

3. Тест работоспособности 
    ```bash 
    curl http://localhost
    ```
    Ожидаемый ответ: Hello from Effective Mobile!

Дополнительно есть возможность создания файла .env для изменения внешнего порта nginx
    ``` 
    NGINX_PORT = 1-65535
    ```

## Архитектура
**Nginx** - reverse-proxy, принимает запросы на порт 80 (или тот, что определён с помощью переменной) и перенаправляет на backend. Nginx передаёт заголовки Host, X-Real-IP, X-Forwarded-For.
**Backend** - простой HTTP-сервер на Python, слушает порт 8080 внутри контейнера. **Порт не публикуется.**
**Сетевое взаимодействие** - сеть Docker (internal).

## Стек проекта
- Docker, Docker Compose
- Python 3.10.20 (Alpine)
- Nginx 3.23 (Alpine-slim)

## Дополнительно
- Backend запускается от непривилегированного пользователя
- Healtcheck для backend
- Отдельная сеть для сервисов
- Минимальный размер образов
