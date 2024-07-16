@echo off

set PYTHON_VER=3.9

:: Проверка соотвествия версии python с рекомендуемой версией.
python --version 2>nul | findstr /b /c:"Python %PYTHON_VER%" >nul
if errorlevel 1 (
    echo Warning: Version python %PYTHON_VER% recommended.
)

IF NOT EXIST venv (
    echo creating venv...
    python -m venv venv
)

:: Создание папки logs.
mkdir ".\logs\setup" > nul 2>&1

:: Установка стандартных настроек конфигурации
python.exe config_file.py

:: Чтение значения переменной UPLOAD_DIR_BOUQUET из config.json
for /f "delims=" %%i in ('python read_config.py') do set "UPLOAD_DIR_BOUQUET=%%i"

:: Вывод значения переменной UPLOAD_DIR_BOUQUET (для отладки)
echo UPLOAD_DIR_BOUQUET is %UPLOAD_DIR_BOUQUET%

:: Создание папки по пути переменной UPLOAD_DIR_BOUQUET
mkdir "%UPLOAD_DIR_BOUQUET%" > nul 2>&1

:: Деактивация активной среды.
call .\venv\Scripts\deactivate.bat

:: Вызов внешней программы Python для проверки локальных модулей.
python .\setup\check_local_modules.py

call .\venv\Scripts\activate.bat

REM Проверка, запуск двойным кликом .bat файла.
IF /i "%comspec% /c %~0 " equ "%cmdcmdline:"=%" (
    REM echo Скрипт был запущен двойным кликом.
    cmd /k python .\setup\setup_windows.py
) ELSE (
    REM echo Скрипт запущен камандной строкой.
    python .\setup\setup_windows.py
)

:: Деактивация вирутальной среды
call .\venv\Scripts\deactivate.bat