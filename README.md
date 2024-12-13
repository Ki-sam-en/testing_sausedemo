#### Тестирование авторизации сайта sausedemo
ссылка на сайт: "http://www.saucedemo.com/v1"

в этом репозитории код для автоматизации тест-кейса по авторизации и аутентификации сайта sausedemo с помощью selenium и pytest. 
также автоматизировала процесс разлогирования с сайта, добавила выбор браузера и минимальный отчет allure в фикстурах.

файл с тестированием аутентификации: test_auth.py

файл с тестированием разлогирования: test_logout.py

файл с фикстурами и надстройкой allure: constest.py

##### скрипт для запуска тестов
![image](https://github.com/user-attachments/assets/0c3ba790-f78c-436b-b3a4-ba1a1369384d)

необходимые библиотеки подгружены локально в venv. скрипт для вызова теста с учетом выбора браузера: 
"$ pytest -vs --browser chrome work_dir\test_dir\test_logout.py" или "$ pytest -vs --browser farefox work_dir\test_dir\test_logout.py"

"$ pytest -vs --browser chrome work_dir\test_dir\test_auth.py" или "$ pytest -vs --browser farefox work_dir\test_dir\test_auth.py"


