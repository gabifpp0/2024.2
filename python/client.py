import http.client

def fazer_requisicao_get():
    # Conectar ao servidor localhost na porta 8000
    conexao = http.client.HTTPConnection("localhost", 8000)

    # Fazer a requisição GET
    conexao.request("GET", "/")

    # Obter a resposta
    resposta = conexao.getresponse()

    # Ler o conteúdo da resposta
    conteudo = resposta.read()

    # Imprimir o status e o conteúdo da resposta
    print(f"Status: {resposta.status}")
    print(f"Motivo: {resposta.reason}")
    print("Conteúdo:")
    print(conteudo.decode("utf-8"))

    # Fechar a conexão
    conexao.close()

# Chamar a função para fazer a requisição GET
fazer_requisicao_get()