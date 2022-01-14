import requests
import json
import time


def buscar_dados():
    request = requests.get("https://api.pancakeswap.info/api/v2/tokens/0x50332bdca94673F33401776365b66CC4e81aC81d")
        # print(request.content)
    jsonFormatado = json.loads(request.content)
    valorCCAR = (jsonFormatado.get("data").get("price"))

    priceReal = requests.get("https://economia.awesomeapi.com.br/json/last/USD")
    jsonReal = json.loads(priceReal.content)
    valorReal = (jsonReal.get("USDBRL").get("high"))

    valorCCARfloat = float(valorCCAR) 

    valorRealfloat = float(valorReal)

    conversao = valorCCARfloat * valorRealfloat

    print(f'A cotação de um CCAR para o valor do REAL atualmente é : R$%.2f' %conversao )

        

while True:
    time.sleep(10)
    if __name__ == '__main__':
        buscar_dados()