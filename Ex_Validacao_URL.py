# Exemplos de URLs válidas:
#     bytebank.com/cambio
#     bytebank.com.br/cambio
#     www.bytebank.com/cambio
#     www.bytebank.com.br/cambio
#     http://www.bytebank.com/cambio
#     http://www.bytebank.com.br/cambio
#     https://www.bytebank.com/cambio
#     https://www.bytebank.com.br/cambio
#
# Exemplos de URL inválidas:
#     https://bytebank/cambio
#     http://bytebank.naoexiste/cambio
#     ht:bytebank.naoexiste/cambio

#https://www.bytebank.com.br/cambio

import re

url = "https://www.bytebank.com.br/cambio"
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
verifica_match = padrao_url.match(url)

if not verifica_match:
    raise ValueError("URL Inválida.")
print("URL válida.")

