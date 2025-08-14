from typing import Optional
from pydantic import Basemodel, HttpUrl

class ArtigoSchema(Basemodel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    url_fonte: HttpUrl
    usuario_id: Optional[int]

    class Config:
        orm_mode = True