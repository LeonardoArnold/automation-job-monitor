from services.api_client import APIClient

client = APIClient()
resultado = client.fetch_data()

print(f"Status: {resultado['status']}")
print(f"Duração: {resultado['duration']}s")
if resultado['status'] == 'success':
    print(f"Total de produtos recuperados: {len(resultado['data']['products'])}")
else:
    print(f"Erro: {resultado['error']}")