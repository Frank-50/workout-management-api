from sqlalchemy import create_engine
from sqlalchemy.orm import session, sessionmaker, DeclarativeBase
from app.core.config import settings


#configuração do engine que gerencia o motor de conecção ccom o banco de dados
engine = create_engine(settings.DATABASE_URL)

# a fabrica de sessões, onde cada sessão e uma conversa com o banco de dados(consultas, inserções, commits)
sessionlocal = sessionmaker(
    bind=None,
    autoflush=True,
    expire_on_commit=True,
    autocommit=False 
)

# A classe que todos os modelos vão herdar 
class Base(DeclarativeBase):

    pass

# A dependencia do FastAPI que abre uma sessão e entrega a rota (yield) e garante que ela seja fechada no final, mesmo em caso de erro
# Todas as rotas vão usar: db: session = depends(get_db)
def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()
