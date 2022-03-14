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
python3 -m pytest -n 2 --reruns 1 --language=en --browser_name=chrome --alluredir=allure-report -m need_review
```
4. Сгенерировать отчет allure
```
allure serve allure-report/
```