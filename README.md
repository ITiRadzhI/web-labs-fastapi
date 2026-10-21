# Лабораторная работа №2: асинхронная SQLite через SQLAlchemy

Это продолжение первой лабораторной с теми же пятью маршрутами. Python 3.11+. Из корня проекта в PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn app.main:app --reload
```

Документация: http://127.0.0.1:8000/docs
Тестирование: `pytest -q`. Данные хранятся в файле `app.db` и остаются после перезапуска.

SQLite создаётся автоматически при запуске приложения. Для лабораторной №3 вместо `create_all` будут введены миграции Alembic.
Рекомендуемая ветка Git: `lab-02-database`. Не публикуйте `.env` и `app.db`.
