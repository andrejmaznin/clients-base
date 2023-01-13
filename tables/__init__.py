import sqlalchemy

from .user import create_table as create_user_table

metadata = sqlalchemy.MetaData()

user = create_user_table(metadata)
