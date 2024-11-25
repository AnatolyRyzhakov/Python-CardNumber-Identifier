# CardNumber Identifier

EN: Web application for BIN-based bank identification

RU: Веб-Приложение, позволяющее идентифицировать банк по BIN номеру

### Requirements

- Pytnon v3.12
- Google Chrome Browser v131
- Docker v25 (optional)

### How to use it?

- Local
- Docker Image (optional)

EN: **Local Run**

1. Clone the repository locally using the command ```git clone https://github.com/AnatolyRyzhakov/Python-CardNumber-Identifier.git```
2. Navigate to the repository's root directory.
3. Create a Python virtual environment: ```python -m venv .venv```
4. Activate the Python virtual environment: ```.venv\Scripts\activate```
5. Install the necessary Python dependencies: ```pip install -r requirements.txt```
6. Run the Flask application: ```flask --app app run```
After successful launch:
    - The console should display a corresponding message.
    - The web page should be accessible in your browser at ```http://127.0.0.1:5000```
- To run the tests, use the command ```pytest -v .\tests```

RU: **Лоальный запуск**

1. Склонировать репозиторий локально с помощью команды ```git clone https://github.com/AnatolyRyzhakov/Python-CardNumber-Identifier.git```
2. Перейти в корневую директорию репозитория
3. Создать виртуальное окружение Python ```python -m venv .venv```
4. Включить использование виртуального окружения Python ```.venv\Scripts\activate```
5. Установить необходимые зависимости для Python ```pip install -r requirements.txt```
6. Запустить Flask приложение ```flask --app app run```
В случае успешного запуска:
    - В консоли должна отобразиться соответствующая информация
    - В браузере должна быть доступна веб-страница, по адресу ```http://127.0.0.1:5000```
- Запуск тестов осуществляется с помощью команды ```pytest -v .\tests```

EN: **Docker (optional)**

1. Build the Docker container using the command ```docker build -t cardnumber-identifier .```
2. Run the built Docker container using the command ```docker run -p 5000:5000 cardnumber-identifier```
If successful:
    - the web application will be accessible at ```http://127.0.0.1:5000```

RU: **Docker (optional)**

1. Собрать Docker контейнер с помощью команды ```docker build -t cardnumber-identifier .```
2. Запустить собранный Docker контейнер командой ```docker run -p 5000:5000 cardnumber-identifier```
В случае успешного запуска:
    - В браузере должна быть доступна веб-страница, по адресу ```http://127.0.0.1:5000```
- Запуск тестов осуществляется с помощью команды ```docker exec -it <CONTAINER ID> .venv/bin/pytest -s tests/```, где ```<CONTAINER ID>``` это ID запущенного контейнера (проверить можно командой ```docker ps```)

### TO DO List

Ideas to upgrade/polishing service

- [ ] Install Chromewebdriver in Dockerfile (to fix UI tests)
- [ ] Add logger and save output to a .log file
- [ ] Add server caching for requests
- [ ] Add more OOP
- [ ] Pretty web UI
- [ ] Async HTTP
- [ ] Autotests Refactoring (make helpers, POM pattern and other)
- [ ] Add more stability and tests (try-except)
- [ ] Optimize DB (replace current realisations to generator)
- [ ] Rename repo and app (because it's wrong)
