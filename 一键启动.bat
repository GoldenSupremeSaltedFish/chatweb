@echo off
REM 启动 Flaskback.py
start python Flaskback.py

REM 等待 5 秒
timeout /t 5 /nobreak

REM 在默认浏览器中打开 http://127.0.0.1:5000/
start http://127.0.0.1:5000/