criando projeto
python -m venv fastapi

usando sistema
.\Scripts\Activate.ps1
saindo
deactivate

instalações
pip install fastapi psycopg2-binary sqlalchemy asyncpg uvicorn python-jose[cryptography] pytz passlib python-multipart
pip install pydantic-settings pydantic[email]

banco de dados usado
docker run --name postgres-container -e POSTGRES_USER=user -e POSTGRES_PASSWORD=admin -e POSTGRES_DB=faculdade -p 5432:5432 -d postgres