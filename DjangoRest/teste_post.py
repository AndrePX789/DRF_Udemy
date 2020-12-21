import requests

headers = {'Authorization' : 'Token b5def6742fce5d5215c75d26e94c49756666e77b'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

novo_curso = {
    "titulo" : "Novo Curso",
    "url" : "http://www.novocurso.com.br"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

#Testando código  de status HTTP 201
assert resultado.status_code == 201

#Testando se o título do curso retornado é o mesmo do informado
assert resultado.json()['titulo'] == novo_curso['titulo']