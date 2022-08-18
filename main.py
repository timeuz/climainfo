import os
import requests
from flask import Flask, Request, jsonify, json

API_KEY = '2663e2bbd329aa8ccb641c1b9e05ae98'

app = Flask(__name__)

@app.route("/<cidade>")

def mostra_temp(cidade):
    #cidade = input('Digite o nome da cidade: ')
    link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br'
    requisicao = requests.get(link)
    result = requisicao.json()
    descricao = result['weather'][0]['description']
    temp_atual = result['main']['temp']
    temp_max = result['main']['temp_max']
    temp_min = result['main']['temp_min']
    real_feel = result['main']['feels_like']
    #print(f"Nuvens: {descricao}")
    #print(f"Temperatura atual: {temp_atual}")
    #print(f"Temperatura maxima: {temp_max}")
    #print(f"Temperatura minima: {temp_min}")
    #print(f"Sensação termica: {real_feel}")
    #return f"Nuvens: {descricao}"
    return descricao, temp_atual, temp_max, temp_min, real_feel

app.run(host="0.0.0.0", port=2000, debug = False)