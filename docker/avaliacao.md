# Docker compose com Django e banco de dados

## Informações gerais

- Assunto: Docker, conteinizar aplicativos
- Disciplina: *sistemas operacionais*
- **Tarefa**:
  1. Criar um projeto django com uma aplicação web
    - alternativa, criar uma _branch_ no repositório do projeto integrador para configurar o acesso ao repositório de dados
  2. Criar um `Dockerfile` para o projeto django
  3. Criar a imagem e testar o conteiner para testar
  4. OPCIONAL, porque dependendo de como pergunta ao assistente de IA; criar um `Dockerfile` para o repositório de banco de dados
  5. Criar um `docker-compose.yml` e configurar para 2 serviços: `webapp` e `db`
  6. Configurar o arquivo django de acesso ao repositório de dados para usar o serviço docker `db`
  7. Testar o `docker-compose.yml`
  8. Relatar minimamente o que foi feito.
- **Entrega**: copia desse aquivo markdown preenchido, no seu repositório _fork_ de https://github.com/sistemas-operacionais/2024.2


## Relatório
Repositório: https://github.com/tads-cnat/TaSeguro/tree/docker
### Aluno

- nome: Gabrielle Fernandes Paiva Pereira
- matrícula: 20241014040003

### Relato
Neste projeto, configuramos um ambiente Docker para rodar uma aplicação Django com um banco de dados PostgreSQL. Utilizamos o docker-compose para definir dois serviços: um para o webapp Django e outro para o banco de dados. A seguir, estão os detalhes dos arquivos de configuração e as etapas realizadas.
### Arquivos docker e de configuração do django
## Dockerfile
O Dockerfile abaixo define a configuração para a construção da imagem Docker para o projeto Django. Ele inclui a instalação das dependências necessárias, como o PostgreSQL client e bibliotecas de imagem, e executa a aplicação Django.

`Dockerfile`

```Dockerfile
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    libwebp-dev \
    libpng-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY requirements.txt .

RUN echo "Conteúdo do requirements.txt:" && cat requirements.txt

RUN pip install --no-cache-dir -r requirements.txt || (echo "Erro ao instalar dependências"; cat requirements.txt; exit 1)

COPY . .

CMD ["python", "mysite/manage.py", "runserver", "0.0.0.0:8000"]

```

## Docker compose

O arquivo docker-compose.yml define a configuração para rodar os containers do Django e PostgreSQL. Ele também configura as variáveis de ambiente necessárias para a comunicação entre o Django e o banco de dados

`docker-compose.yml`

```yaml
services:
  webapp:
    image: mysite-django
    build: .
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://myuser:mypassword@db:5432/mydb
    depends_on:
      - db
    command: >
      sh -c "sleep 10 && python mysite/taseguro/manage.py migrate && python mysite/taseguro/manage.py runserver 0.0.0.0:8000"

  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=myuser
      - POSTGRES_PASSWORD=mypassword
      - POSTGRES_DB=mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres_data:
```

O processo de configuração com Docker e Docker Compose foi concluído com sucesso, permitindo que a aplicação Django interaja com o banco de dados PostgreSQL de maneira eficiente e isolada, em containers. O ambiente foi testado e validado, garantindo que o projeto pode ser facilmente executado em qualquer máquina que tenha o Docker instalado.

**observação** coloque nomes nos arquivos antes do códigos-fonte.
