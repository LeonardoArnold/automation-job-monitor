from automation.web_bot import WebBot

print("🚀 Iniciando o teste do robô...")
bot = WebBot()
resultado = bot.run_automation()

print("-" * 30)
print(f"Status Final: {resultado['status']}")
if resultado['status'] == 'success':
    print(f"✅ Sucesso! O robô rodou em {resultado['duration']}s")
else:
    print(f"❌ Erro: {resultado['error']}")