import sqlalchemy

from .user import create_table as create_user_table
from .auth_user import create_table as create_auth_user_table

metadata = sqlalchemy.MetaData()

user = create_user_table(metadata)
auth_user = create_auth_user_table(metadata)
