# Лабораторная работа №1: FastAPI и CRUD в памяти

Python 3.11+. Из корня папки проекта в PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Документация: http://127.0.0.1:8000/docs
Тесты: `pytest -q`. После перезапуска сервера список задач обнуляется.
Для следующей лабораторной используйте проект lab-02: он продолжает тот же API, но данные сохраняет в SQLite.

Рекомендуемая ветка Git: `lab-01-basic-api`.
