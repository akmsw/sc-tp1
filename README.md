# Calculadora de cotización de criptomonedas

## Brief
El siguiente es un trabajo práctico que consta de una calculadora de cotización de criptomonedas. Se provee al usuario un menú simple donde podrá elegir la criptomoneda en cuestión y la moneda a la cual su valor se convertirá.

## Details
Las consultas a la API [Alpha Vantage](https://www.alphavantage.co/) y el menú se desarrollaron en Python para facilitar el código. Con los resultados obtenidos, corremos un programa en C que se encarga de pasar los parámetros a un programa en Assembly que realiza las operaciones matemáticas necesarias para realizar la conversión, retornando a C el valor calculado listo para mostrar en pantalla.
