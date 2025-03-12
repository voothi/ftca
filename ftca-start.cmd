@echo off
timeout /t 1 /nobreak > NUL

echo Starting ftca.py...
start http://127.0.0.1:5010/?clipboard=true^&s=test
start cmd /c "cd /d .\ && python.exe .\ftca.py"
