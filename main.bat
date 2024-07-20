@echo off

:: Деактивация активной среды
call .\venv\Scripts\deactivate.bat

:: Проверка на локальные модули
python .\setup\check_local_modules.py --no_question

:: Активация виртуальной среды
call .\venv\Scripts\activate.bat
set PATH=%PATH%;%~dp0venv\Lib\site-packages\torch\lib

:: Валидация requirements
python.exe .\setup\validate_requirements.py

:: Очистка setup.log
python.exe clear_setup_log.py

:: Запускает сервер main.py.
if %errorlevel% equ 0 (
    REM Был ли запущен батник двойным кликом?
    IF /i "%comspec% /c %~0 " equ "%cmdcmdline:"=%" (
        REM echo Этот скрипт был запущен двойным кликом.
	cmd /k uvicorn main:app %*
    ) ELSE (
        REM echo Этот скрипт был запущен с помощью командной строки.
        uvicorn main:app %*
    )
)
