import requests

# GET Avaliacoes

#avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

#Acessando o código de status HTTP
#print(avaliacoes.status_code)

#Acessando os dados da resposta
#print(avaliacoes.json())
#print(type(avaliacoes.json())) Dict

#Acessando a quantidade de registros
#print(avaliacoes.json()['count'])

#Acessando a proxima página de resultados
#print(avaliacoes.json()['next'])

#Acessando os resultados desta página
#print(avaliacoes.json()['results']) Retorna um Lista


#Acessando a segunda página
#avaliacoespg2 = requests.get(avaliacoes.json()['next'])
#print(avaliacoespg2.json()['results'])

#GET cursos
headers = {'Authorization': 'Token b5def6742fce5d5215c75d26e94c49756666e77b'}

cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)
print(cursos)