@echo off
title AgriSmart AI Server Launcher
color 0A
cls
echo ============================================================
echo         AGRISMART AI - CONTINUOUS SERVER LAUNCHER
echo ============================================================
echo.
echo [1/3] Checking Python environment...
python -c "import flask" >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Flask not detected! Please ensure python is installed.
    pause
    exit /b
)

echo [2/3] Checking Port 5000...
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :5000 ^| findstr LISTENING') do taskkill /f /pid %%a >nul 2>&1

echo [3/3] Starting Flask Application...
start /b python app.py > app_server.log 2>&1
timeout /t 2 /nobreak >nul

echo.
echo ============================================================
echo   SERVER IS LIVE AND RUNNING!
echo ============================================================
echo.
echo   [LAPTOP BROWSER]
echo   http://127.0.0.1:5000
echo.
echo   [MOBILE BROWSER - SAME WI-FI (PERMANENT)]
echo   http://192.168.31.202:5000
echo.
echo ============================================================
echo   Starting Cloudflare Live Mobile Tunnel...
echo ============================================================
echo.

:TUNNEL_LOOP
.\cloudflared.exe tunnel --url http://127.0.0.1:5000
echo.
echo [INFO] Tunnel disconnected. Reconnecting in 3 seconds...
timeout /t 3 /nobreak >nul
goto TUNNEL_LOOP
