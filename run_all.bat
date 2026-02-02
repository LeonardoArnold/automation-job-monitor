@echo off
title Monitor de Vagas - Sicredi
echo ==========================================
echo   INICIANDO SISTEMA DE MONITORAMENTO
echo ==========================================

:: 1. Garante que o script rode na pasta correta
set BASE_DIR=%~dp0
cd /d %BASE_DIR%

:: 2. Inicia a API em uma nova janela
echo [INFO] Iniciando API FastAPI...
start cmd /k "title API Status && cd /d %BASE_DIR% && venv\Scripts\python.exe -m uvicorn api.app:app"

:: 3. Pausa de 5 segundos para a API subir
timeout /t 5 /nobreak > nul

:: 4. Executa o fluxo de monitoramento
echo [INFO] Iniciando Fluxo de Automacao (Prefect)...
venv\Scripts\python.exe -m flows.job_flow

echo ==========================================
echo   EXECUCAO CONCLUIDA!
echo ==========================================
pause