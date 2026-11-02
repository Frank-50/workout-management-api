
# Workout-manegement-api
## Projeto que visa a criação de uma **API de gerenciamento de treino** e controle das Atividades **FITNESS**

> projeto em desenvolvimento

## tecnologias

- Python
- FastAPI
- PostgreSQL
- SQLAlchame
- Pytest

## Como rodar localmente

### 1. Clonar o repositorio e criar o ambiente virtual

```bash
git clone <url-do-repositorio>
cd workout-manegement-api
python -m venv .venv
.venv\scripts\activate         # Windows
# source .venv/bin/activate    #Linux/Mac

pip install -r requirements.txt
```

### 2. Configurar o postgreSQL
conectado como superusuário ('postgres'), crie o usuário e o banco de desenvolvimento:

```SQL
CREATE USER training_user WITH LOGIN PASSWORD 'criar_senha_aqui' CREATEDB; 
CREATE DATABASE training_db OWNER training_user;

# LOGIN | CREATEDB - são responsaveis por dar permição de crair bancos de dados ao usuário
```

### 3. configurar as variáveis de ambiente

copie o modelo e preencha com a suas variáveis de ambiente

```bash
cp .env.example .env     # no Powershell: copy .env.example .env
```

edite o `.env`

```
DATABESE_URL=postgresql+psycopg2://training_user:sus_senha@localhoste:5432/training_db
SECRET_KEY=<gere com: python -c "import secrets; pint(secrets.token_hex(32))">
```

### 4. Subir a API 

```bash
uvicorn app.main:app --reload
```

A documentação interativa fica em `http://localhost:8000/docs`