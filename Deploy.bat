CALL .\.venv\Scripts\activate
START /MIN python .\manage.py runserver 8008
timeout 5
explorer http://localhost:8008/login/