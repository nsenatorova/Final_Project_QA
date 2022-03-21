# Final_Project_for_Stepik
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
3. Запустить тесты для ревью
```
python3 -m pytest -n 2 --reruns 1 --language=en --browser_name=chrome --window=1366,768 --headless=false --alluredir=allure-report -m need_review
```
Если параметр размера окна не был передан, при запуске тестов будет использоваться размер окна 1920×1080; если не был передан параметр headless, браузер дефолтно будет запускаться в headless режиме
4. Сгенерировать отчет allure
```
allure serve allure-report/
```