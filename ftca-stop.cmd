@echo off
timeout /t 1 /nobreak > NUL

echo Stopping ftca.py processes...
powershell.exe -NoProfile -Command ^
"& { ^"
    ^$pythonProcesses = Get-WmiObject -Query 'SELECT * FROM Win32_Process WHERE Name = "python.exe" AND CommandLine LIKE "%ftca.py%"'; ^
    foreach (^$process in ^$pythonProcesses) { ^
        echo Killing process ^$process.Handle; ^
        taskkill /F /PID ^$process.Handle; ^
        ^$parentProcess = Get-WmiObject -Query "SELECT * FROM Win32_Process WHERE ProcessId = ^$process.ParentProcessId"; ^
        if (^$parentProcess) { ^
            echo Killing parent process ^$parentProcess.Handle; ^
            taskkill /F /PID ^$parentProcess.Handle; ^
        } ^
    } ^
"}"

if %errorlevel% equ 0 (
    echo Successfully stopped ftca.py processes.
) else (
    echo Failed to stop ftca.py processes.
)
