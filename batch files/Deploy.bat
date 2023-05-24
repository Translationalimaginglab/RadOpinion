CALL ..\.venv\Scripts\activate
START /MIN python ..\manage.py runserver 8008
timeout 10
explorer http://localhost:8008/login/