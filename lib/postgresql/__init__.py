from databases import Database
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine

from lib.postgresql.settings import PostgreSQLSettings

load_dotenv()

psql_settings = PostgreSQLSettings()
PSQL_CONNECTION_URL = psql_settings.construct_connection_url(driver='postgresql+asyncpg')
print(f'connecting to {PSQL_CONNECTION_URL}')
database = Database(PSQL_CONNECTION_URL)
engine = create_async_engine(PSQL_CONNECTION_URL)


def get_connection():
    return database
