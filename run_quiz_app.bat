@echo off
cd /d "C:\Users\saira\Desktop\FAM\RAM\prompt eng\quiz app"
call venv\Scripts\activate
start python manage.py runserver
timeout /t 5 /nobreak > NUL
start http://127.0.0.1:8000
pause

