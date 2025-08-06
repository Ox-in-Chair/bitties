@echo off
if "%~1"=="" (
    echo Usage: commit "Your message"
    exit /b 1
)
python bitties_commit.py %*