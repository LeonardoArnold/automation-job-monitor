from prefect import task, flow
from services.api_client import APIClient
from automation.web_bot import WebBot
import datetime
import json
import os

# Definimos as Tarefas (Tasks)
@task(retries=2, retry_delay_seconds=5)
def task_api_check():
    client = APIClient()
    return client.fetch_data()

@task(retries=1)
def task_web_automation():
    bot = WebBot()
    return bot.run_automation()

@task
def monitor_sla(api_res, bot_res):
    # Regra de SLA: O processo total não deve passar de 20 segundos
    total_duration = api_res['duration'] + bot_res['duration']
    sla_limit = 20.0
    
    status = "DENTRO_DO_SLA" if total_duration <= sla_limit else "VIOLAÇÃO_DE_SLA"
    
    # Criamos o relatório incluindo as vagas coletadas pelo bot
    report = {
        "timestamp": datetime.datetime.now().isoformat(),
        "total_duration": total_duration,
        "sla_status": status,
        "details": {
            "api": api_res['status'],
            "web": bot_res['status'],
            "vagas_encontradas": bot_res.get('msg', 'Nenhuma vaga listada') # Puxa as vagas do web_bot
        }
    }
    
    # Garante que a pasta logs existe
    if not os.path.exists("logs"):
        os.makedirs("logs")
        
    # Salva o relatório completo para a API ler
    with open("logs/last_run.json", "w") as f:
        json.dump(report, f, indent=4)
    
    print(f"--- RELATÓRIO DE MONITORAMENTO ATUALIZADO ---\n{report}")
    return report

# O Maestro: O Fluxo que une tudo
@flow(name="Automation Job Monitor Flow")
def main_flow():
    # 1. Busca dados na API
    api_data = task_api_check()
    
    # 2. Roda automação se a API estiver OK
    if api_data['status'] == "success":
        bot_data = task_web_automation()
        
        # 3. Monitora o SLA e gera log
        monitor_sla(api_data, bot_data)
    else:
        print("Fluxo interrompido: API falhou.")

if __name__ == "__main__":
    main_flow()