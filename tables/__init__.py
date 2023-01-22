import sqlalchemy

from .user import create_table as create_user_table
from .occupation import create_table as create_occ_table
from .client import create_table as create_client_table

metadata = sqlalchemy.MetaData()

user = create_user_table(metadata)
occupation = create_occ_table(metadata)
client = create_client_table(metadata)