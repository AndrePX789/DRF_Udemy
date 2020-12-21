import requests

headers = {'Authorization' : 'Token b5def6742fce5d5215c75d26e94c49756666e77b'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url_base_cursos, headers=headers)

#Testando se o endpoint está correto
assert resultado.status_code == 200

#Testando a quantidade de registros
assert resultado.json()['count'] == 8

#Testando se o titulo do primeiro curso está correto
assert resultado.json()['results'][0]['titulo'] == "Criação de Api's Rest com Django Rest Framework" 