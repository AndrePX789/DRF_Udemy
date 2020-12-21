import requests

class TestCursos:
    headers = {'Authorization' : 'Token b5def6742fce5d5215c75d26e94c49756666e77b'}
    url_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        cursos = requests.get(url=self.url_cursos, headers=self.headers)

        assert cursos.status_code == 200

    def test_get_curso(self):
        curso = requests.get(url=f'{self.url_cursos}1/', headers=self.headers)

        assert curso.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo" : "Novo Curso",
            "url" : "http://www.novocurso.com.br"
        }
        resposta = requests.post(url=self.url_cursos, headers=self.headers, data=novo)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            "titulo" : "Novo Novo Curso",
            "url" : "http://www.novonovocurso.com.br"
        }

        resposta = requests.put(url=f'{self.url_cursos}10/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 200
        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_cursos}10/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0