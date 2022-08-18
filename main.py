import os
import requests
from flask import Flask, Request, jsonify, json

API_KEY = '2663e2bbd329aa8ccb641c1b9e05ae98'

app = Flask(__name__)

@app.route("/<cidade>")

def mostra_temp(cidade):

    link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br'
    requisicao = requests.get(link)
    
    result = json.loads(requisicao.text)
    
    teste = {
        "descricao" : result['weather'][0]['description'],
        "temp_atual" : result['main']['temp'],
        "temp_max" : result['main']['temp_max'],
        "temp_min" : result['main']['temp_min'],
        "real_feel" : result['main']['feels_like']
    }
    
    return teste

app.run(host="0.0.0.0", port=2000, debug = True)