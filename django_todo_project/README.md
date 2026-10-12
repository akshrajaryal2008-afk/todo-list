# Django To-Do Web App

## Windows setup

1. Install Python 3.10+.
2. Extract this folder and open a terminal inside it.
3. Create and activate a virtual environment:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, use Command Prompt:
   `venv\Scripts\activate.bat`

4. Install Django:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Create the database:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Start the site:

   ```bash
   python manage.py runserver
   ```

7. Open http://127.0.0.1:8000/ in your browser.

Features: add, edit, delete, and clear all tasks.
