@echo off
setlocal

pyinstaller --onefile --icon=icon.ico --name=a2sm main.py

endlocal
