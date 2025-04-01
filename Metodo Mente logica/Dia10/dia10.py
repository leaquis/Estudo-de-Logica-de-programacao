import math

numero = 16
raiz_quadrada = math.sqrt(numero)
print(raiz_quadrada)

from math import pi
print(f"O valor de pi é {pi}")

import math as m
print(f"O coseno de 0 é {m.cos(0)}")


import random

dado = random.randint(1, 6)
print(f"O valor do dado é {dado}")


from datetime import datetime

agora = datetime.now()

print(agora)


import os
arquivos = os.listdir('.')

print(f"Os arquivos dessa pasta são: {arquivos}")


import sys

print(f"A versão do Python é: {sys.version}")


import meu_modulo

mensagem = meu_modulo.saudacao("Giovani")
print(mensagem)

resultado = meu_modulo.soma(5, 7)
print(f"A soma é {resultado}")


import requests
resposta = requests.get('https://api.github.com')
print(f"Status da resposta: {resposta.status_code}")
