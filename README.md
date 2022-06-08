Репозиторий для последнего проекта на курсе "Автоматизация тестирования с помощью Selenium и Python"
### Шаги для установки и запуска проекта
1. Скачать репозиторий
```
git clone https://github.com/nsenatorova/Final_Project_for_Stepik.git
```
2. Установить требуемые пакеты
```
pip install -r requirements.txt
```
3. Запустить тесты для ревью. Если параметр размера окна не был передан, при запуске тестов будет использоваться размер окна 1920×1080; если не был передан параметр headless, браузер дефолтно будет запускаться в headless режиме
```
python3 -m pytest -n 2 --reruns 1 --language=en --browser_name=chrome --window=1366,768 --headless=false --alluredir=allure-report -m need_review
```
4. Сгенерировать отчет allure
```
allure serve allure-report/
```
Для запуска тестов (Chrome) в Docker-контейнере:
```
docker build --tag project .   

docker-compose up -d tests allure
```
После запуска контейнера allure новый отчет будет доступен на http://localhost:5050/allure-docker-service/latest-report
