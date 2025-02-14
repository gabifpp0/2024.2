import http.server

# Definir o conteúdo HTML fixo
html_fixo = """
<!DOCTYPE html>
<html>
<head>
    <title>Servidor HTTP Multithread</title>
</head>
<body>
    <h1>Olá, mundo!</h1>
    <p>Este é um servidor HTTP multithread em Python.</p>
</body>
</html>
"""

class MeuManipulador(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Imprimir informações da requisição no console
        print(f"Requisição recebida de: {self.client_address}")
        print(f"Caminho solicitado: {self.path}")
        print("Cabeçalhos da requisição:")
        for nome, valor in self.headers.items():
            print(f"{nome}: {valor}")

        # Enviar resposta de código 200
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # Enviar o conteúdo HTML fixo
        self.wfile.write(html_fixo.encode("utf-8"))

# Definir o endereço e a porta do servidor
endereco = ("", 8000)

# Criar o servidor
with http.server.HTTPServer(endereco, MeuManipulador) as httpd:
    print("Servidor HTTP rodando na porta 8000...")
    # Manter o servidor rodando
    httpd.serve_forever()