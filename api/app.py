from fastapi import FastAPI
import json
import os

app = FastAPI(title="Automation Job Monitor API")

LOG_FILE = "logs/last_run.json"

@app.get("/")
def home():
    return {"message": "API de Monitoramento Sicredi - Ativa"}

@app.get("/status")
def get_status():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    return {"error": "Nenhuma execução encontrada ainda."}