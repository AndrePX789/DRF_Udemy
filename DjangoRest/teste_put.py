import requests

headers = {'Authorization' : 'Token b5def6742fce5d5215c75d26e94c49756666e77b'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo" : "Novo Novo Curso",
    "url" : "http://www.novocurso.com.br"
}

#Buscado o curso pelo ID
#curso = requests.get(url=f'{url_base_cursos}9/', headers=headers)
#print(curso.json())

resultado = requests.put(url=f'{url_base_cursos}9/', headers=headers, data=curso_atualizado)

#Testando código de status HTTP 200
assert resultado.status_code == 200

#Testando Titulo
assert resultado.json()['titulo'] == curso_atualizado['titulo']