import requests

headers = {'Authorization' : 'Token b5def6742fce5d5215c75d26e94c49756666e77b'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}9/', headers=headers)


#Testando código HTTp
assert resultado.status_code == 204

#Testadno se o tamanho do conteudo é 0
assert len(resultado.text) == 0