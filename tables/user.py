from sqlalchemy import Column, text, MetaData, Table, String, Boolean, DATE, Index
from sqlalchemy.dialects.postgresql import UUID


def create_table(metadata: MetaData) -> Table:
    user = Table(
        'user',
        metadata,
        Column(
            'id',
            UUID,
            server_default=text('gen_random_uuid()'),
            primary_key=True
        ),
        Column(
            'firstname',
            String
        ),
        Column(
            'password',
            String
        ),
        Column(
            'lastname',
            String
        ),
        Column(
            'phone_number',
            String,
            index=True,
            unique=True
        ),
        Column(
            'email',
            String,
            index=True,
            unique=True
        ),
        Column(
            'birthdate',
            DATE
        ),
        Column(
            'country',
            String
        ),
        Column(
            'city',
            String
        ),
        Column(
            'avatar_url',
            String
        ),
        Column(
            'blocked',
            Boolean,
            default=False
        ),
        Column(
            'confirmed',
            Boolean,
            default=False
        )
    )
    Index(
        'firstname_idx',
        user.c.firstname,
        postgresql_ops={
            'description': 'gin_trgm_ops',
        },
        postgresql_using='gin'
    )
    Index(
        'lastname_idx',
        user.c.lastname, 
        postgresql_ops={
            'description': 'gin_trgm_ops',
        },
        postgresql_using='gin'
    )
    Index(
        'city_idx',
        user.c.city, 
        postgresql_ops={
            'description': 'gin_trgm_ops',
        },
        postgresql_using='gin'
    )
    Index(
        'birthdate_idx',
        user.c.birthdate, 
        postgresql_ops={
            'description': 'gin_trgm_ops',
        },
        postgresql_using='gin'
    )
    return user
