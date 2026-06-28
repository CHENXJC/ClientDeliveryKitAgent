@echo off
setlocal
cd /d "%~dp0\.."

python -c "import streamlit" >nul 2>nul
if errorlevel 1 (
  echo Streamlit is not installed. Run: python -m pip install -r requirements.txt
  exit /b 1
)

python -m streamlit run app.py --server.port 8535
