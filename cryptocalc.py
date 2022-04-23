# Authors: Luna, Lihué Leandro; Bonino, Francisco Ignacio
# Version: 0.2.1
# Since: 2022-03-18

import requests
import subprocess

endloop = 0
crypto = "BTC"
moneda = "ARS"
btc = 0

print("Bienvenido a la calculadora de cotización de criptomonedas!")

while endloop == 0:
    print("Seleccione la criptomoneda a consultar:")
    print("1.BTC")
    print("2.ETH")

    option = input()

    if option == '1':
        crypto = "BTC"
        endloop = 1

    if option == '2':
        crypto = "ETH"
        endloop = 1

endloop = 0

while endloop == 0:
    print("Seleccione la moneda de conversión:")
    print("1.EUR")
    print("2.ARS")
    print("3.USD")

    option = input()

    if option == '1':
       moneda = "EUR"
       endloop = 1

    if option == '2':
        moneda = "ARS"
        endloop = 1

    if option == '3':
       moneda = "USD"
       endloop = 1

if crypto=="BTC":
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=9N3E66AEYSMKXXHT'

if crypto=="ETH":
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=ETH&to_currency=USD&apikey=9N3E66AEYSMKXXHT'

r = requests.get(url)

data = r.json()

cryptoprice = data['Realtime Currency Exchange Rate']['5. Exchange Rate']

if moneda == "ARS":
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=ARS&apikey=9N3E66AEYSMKXXHT'

if moneda == "EUR":
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=EUR&to_currency=USD&apikey=9N3E66AEYSMKXXHT'

if moneda == "USD":
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=USD&apikey=9N3E66AEYSMKXXHT'

r = requests.get(url)

data = r.json()

currencyprice = data['Realtime Currency Exchange Rate']['5. Exchange Rate']

aux = "\nPrecio criptomoneda: {str1}\nPrecio moneda: {str2}".format(str1 = cryptoprice, str2 = currencyprice)

print(aux)

subprocess.run(["./calc",cryptoprice, currencyprice])

file = open("result.txt")

result ="\nEl valor de {str1} en {str2} es: {c}".format(str1 = crypto, str2 = moneda, c = file.read())

print(result)