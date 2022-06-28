import requests
API_KEY = '2663e2bbd329aa8ccb641c1b9e05ae98'

cidade = input('Digite o nome da cidade: ')

link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br'

requisicao = requests.get(link)
result = requisicao.json()
descricao = result['weather'][0]['description']
temp_atual = result['main']['temp']
temp_max = result['main']['temp_max']
temp_min = result['main']['temp_min']
real_feel = result['main']['feels_like']
print(f"Nuvens: {descricao}")
print(f"Temperatura atual: {temp_atual}")
print(f"Temperatura atual: {temp_max}")
print(f"Temperatura atual: {temp_min}")
print(f"Temperatura atual: {real_feel}")