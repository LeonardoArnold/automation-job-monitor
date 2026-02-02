Automation Job Monitor - Sicredi Candidate Project

Sistema de monitoramento inteligente que orquestra automação web e consumo de APIs, focado em observabilidade e cumprimento de SLAs.

> Contexto: Este projeto simula um monitoramento crítico de disponibilidade, unindo extração de dados via Selenium (Web Scraping) e integração técnica via API, tudo orquestrado profissionalmente para garantir resiliência.

Tecnologias Utilizadas:

Python 3.11+: Linguagem base do ecossistema.
Prefect: Orquestração de tarefas com gestão de retentativas (Resiliência) e monitoramento de fluxo.
FastAPI: Disponibilização de status do monitoramento via endpoint REST em tempo real.
Selenium + WebDriverManager: Automação de interface web com técnica de Wait explícito para maior estabilidade.
JSON Persistence: Armazenamento local de logs para histórico de execuções e análise de métricas.

Como Executar:

Opção Rápida (Windows)

Para rodar tudo com um clique, localize na pasta do projeto e abra o arquivo:
run_all.bat

Este comando vai abrir a API e rodar o robô de monitoramento automaticamente.

Execução Manual

* Clone o repositório e acesse a pasta: `cd automation-job-monitor`.
* Ative o ambiente virtual: `.\venv\Scripts\activate`.
* Instale as dependências: `pip install -r requirements.txt`.
* Execute o fluxo de monitoramento: `python -m flows.job_flow`.
* Inicie o servidor da API: `uvicorn api.app:app --reload`.
* Acesse o status em tempo real: `http://127.0.0.1:8000/status`.

Diferenciais Técnicos e Regras de Negócio:

Monitoramento de SLA (Service Level Agreement): O sistema calcula o tempo total de execução. Caso ultrapasse o limite de 20 segundos, o status é automaticamente marcado como `VIOLAÇÃO_DE_SLA`.
Arquitetura Modular: Separação clara entre serviços de API, bots de automação e fluxos de orquestração.
Resiliência e Auto-Recuperação: Utilização de `retries` automáticos no Prefect para lidar com falhas de rede.
Observabilidade: Interface JSON simplificada para consumo por dashboards externos.
