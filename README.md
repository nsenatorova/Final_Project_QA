# Final_Project_for_Stepik
Репозиторий для последнего проекта на курсе "Автоматизация тестирования с помощью Selenium и Python"
### Шаги для установки и запуска проекта
1. Скачать репозиторий
```
git clone https://github.com/nsenatorova/Final_Project_for_Stepik.git
```
2. Установить требуемые пакеты
```
pip install requirements.txt
```
3. В файлах с тестами прописать путь к проекту в строке
```
sys.path.insert(1, '/Users/user/Final_Project_for_Stepik/')
```
4. Запустить тесты для ревью
```
pytest -v --tb=line --language=en -m need_review
```
