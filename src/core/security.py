from passlib.context import CryptContext

CRYPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verificar_senha(senha: str, hash_senha: str) -> bool:
    '''
    função para verificar se a senha está correta
    a senha é informada pelo usuário e o hash estará armazenado no banco
    '''
    return CRYPTO.verify(senha, hash_senha)

def gerar_hash_senha(senha: str) -> str:
    return CRYPTO.hash(senha)