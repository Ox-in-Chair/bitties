@echo off
REM ============================================
REM Bitties Command Reference and Quick Actions
REM ============================================
REM Created: 2025/08/06 19:49:05.15
REM Path: C:\Users\mike\OneDrive\BitcoinApp\bitties

REM To view commands: type bitties_commands.bat
REM To run action: bitties_commands.bat [action]

if "%%1"=="" goto :SHOW_COMMANDS
if "%%1"=="run" goto :RUN_APP
if "%%1"=="git-update" goto :GIT_UPDATE
if "%%1"=="git-status" goto :GIT_STATUS
if "%%1"=="activate" goto :ACTIVATE_VENV
if "%%1"=="install" goto :INSTALL_DEPS
if "%%1"=="test-api" goto :TEST_API
if "%%1"=="backup" goto :BACKUP_DATA
if "%%1"=="handover" goto :UPDATE_HANDOVER
goto :SHOW_COMMANDS

:SHOW_COMMANDS

echo ===== BITTIES COMMAND REFERENCE =====
echo.
echo NAVIGATION:
echo cd C:\Users\mike\OneDrive\BitcoinApp\bitties
echo.
echo VIRTUAL ENVIRONMENT:
echo venv\Scripts\activate                    - Activate virtual environment
echo deactivate                               - Deactivate virtual environment
echo python -m venv venv                      - Create new virtual environment
echo.
echo RUNNING APP:
echo python run.py                            - Start Flask app
echo python -m flask run                      - Alternative Flask start
echo set FLASK_DEBUG=1 && python run.py       - Run in debug mode
echo.
echo DEPENDENCIES:
echo pip install -r requirements.txt          - Install all dependencies
echo pip freeze > requirements.txt            - Update requirements file
echo pip install [package]                    - Install specific package
echo.
echo GIT COMMANDS:
echo git status                               - Check changes
echo git add .                                - Stage all changes
echo git add [file]                           - Stage specific file
echo git commit -m "message"                  - Commit with message
echo git push                                 - Push to GitHub
echo git pull                                 - Pull from GitHub
echo git log --oneline                        - View commit history
echo.
echo FILE OPERATIONS:
echo echo [content] > [file]                  - Create/overwrite file
echo echo [content] >> [file]                 - Append to file
echo type [file]                              - View file contents
echo dir                                      - List directory contents
echo mkdir [folder]                           - Create folder
echo.
echo API TESTING:
echo curl http://localhost:5000/api/status    - Test API status
echo curl http://localhost:5000/api/btc/price - Get BTC price
echo.
echo QUICK ACTIONS:
echo bitties_commands run                     - Start app with venv
echo bitties_commands git-update              - Add, commit, push all
echo bitties_commands git-status              - Check git status
echo bitties_commands activate                - Just activate venv
echo bitties_commands backup                  - Backup data files
echo bitties_commands handover                - Update GPT handover
echo.
goto :END

:RUN_APP
echo Starting Bitties app...
cd /d C:\Users\mike\OneDrive\BitcoinApp\bitties
call venv\Scripts\activate
python run.py
goto :END

:GIT_UPDATE
echo Updating GitHub...
cd /d C:\Users\mike\OneDrive\BitcoinApp\bitties
git add .
git commit -m "Update: %2025/08/06% %19:49:05.16%"
git push
echo GitHub updated!
goto :END

:GIT_STATUS
cd /d C:\Users\mike\OneDrive\BitcoinApp\bitties
git status
goto :END

:ACTIVATE_VENV
cd /d C:\Users\mike\OneDrive\BitcoinApp\bitties
call venv\Scripts\activate
goto :END

:INSTALL_DEPS
cd /d C:\Users\mike\OneDrive\BitcoinApp\bitties
call venv\Scripts\activate
pip install -r requirements.txt
goto :END

:TEST_API
echo Testing API endpoints...
curl http://localhost:5000/api/status
echo.
curl http://localhost:5000/api/btc/price
goto :END

:BACKUP_DATA
echo Backing up data files...
cd /d C:\Users\mike\OneDrive\BitcoinApp\bitties
xcopy app\data\*.json backups\%2025-08-06%\ /Y
echo Data backed up to backups\%2025-08-06%\
goto :END

:UPDATE_HANDOVER
echo Updating GPT Handover...
cd /d C:\Users\mike\OneDrive\BitcoinApp\bitties
call update_handover.bat
goto :END

:END
