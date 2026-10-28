
from fastapi import APIRouter, status 
#define que a classe APIRouter foi atribuida a variavel router
router = APIRouter()

@router.get("/health", status_code=status.HTTP_200_OK)
def saude():
    return {"menssagem": "API rodando com sucesso"}