import requests
import jsonpath


avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')
#resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')
#print(resultados)

#primeira = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')
#print(primeira)

# nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')
# print(nome)

#nota_dada = jsonpath.jsonpath(avaliacoes.json(), 'results[0].avaliacao')
#print(nota_dada)

# Todas as pessoas que avaliaram
nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
print(nomes)