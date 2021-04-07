import re

ceps = 'Estou morando em um lugar com cep 26135-110, 24163-210'

url = 'Acesse o site https://www.google.com.br/ e http://www.g1.com'

print(re.findall('\d{5}-\d{3}', ceps))

print(re.findall('https?://[A-Za-z0-9./]+', url))
