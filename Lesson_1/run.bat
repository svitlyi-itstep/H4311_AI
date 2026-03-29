@echo off

chcp 65001 > nul

set GEMINI_API_KEY=AIzaSyCbsf7V9M8TtN9oXimQSNT0xGw-TSAkjvY

call .venv\Scripts\activate
python main.py

pause
