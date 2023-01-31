from sqlalchemy import Column, text, MetaData, Table, String, DATE, ForeignKey, Index, Integer
from sqlalchemy.dialects.postgresql import UUID, JSONB


def create_table(metadata: MetaData) -> Table:
    client = Table(
        'client',
        metadata,
        Column(
            'id',
            UUID,
            server_default=text('gen_random_uuid()'),
            primary_key=True
        ),
        Column(
            'user',
            ForeignKey('user.id')
        ),
        Column(
            'occupation',
            ForeignKey('occupation.occupation')
        ),
        Column(
            'firstname',
            String
        ),
        Column(
            'lastname',
            String
        ),
        Column(
            'birthdate',
            DATE
        ),
        Column(
            'city',
            String
        ),
        Column(
            'work_place',
            String
        ),
        Column(
            'income',
            Integer
        ),
        Column(
            'imgs',
            JSONB
        ),
        Column(
            'phone_number',
            String
        ),
        Column(
            'email',
            String
        ),
        Column(
            'linkedin',
            String,
            nullable=True
        ),
        Column(
            'vk',
            String,
            nullable=True
        ),
        Column(
            'instagram',
            String,
            nullable=True
        ),
        Column(
            'telegram_id',
            String,
            nullable=True
        )
    )

    Index(
        'income_idx',
        client.c.income,
        postgresql_ops={
            'description': 'gin_trgm_ops',
        },
        postgresql_using='gin'
    )
    Index(
        'occupation_idx',
        client.c.occupation,
        postgresql_ops={
            'description': 'gin_trgm_ops',
        },
        postgresql_using='gin'
    )
    Index(
        'work_place_idx',
        client.c.work_place,
        postgresql_ops={
            'description': 'gin_trgm_ops',
        },
        postgresql_using='gin'
    )
    Index(
        'imgs_idx',
        client.c.imgs,
        postgresql_ops={
            'description': 'gin_trgm_ops',
        },
        postgresql_using='gin'
    )
    Index(
        'email_idx',
        client.c.email,
        postgresql_ops={
            'description': 'gin_trgm_ops',
        },
        postgresql_using='gin'
    )
    Index(
        'firstname_idx',
        client.c.firstname,
        postgresql_ops={
            'description': 'gin_trgm_ops',
        },
        postgresql_using='gin'
    )
    Index(
        'lastname_idx',
        client.c.lastname, 
        postgresql_ops={
            'description': 'gin_trgm_ops',
        },
        postgresql_using='gin'
    )
    Index(
        'city_idx',
        client.c.city, 
        postgresql_ops={
            'description': 'gin_trgm_ops',
        },
        postgresql_using='gin'
    )
    Index(
        'linkedin_idx',
        client.c.linkedin, 
        postgresql_ops={
            'description': 'gin_trgm_ops',
        },
        postgresql_using='gin'
    )
    Index(
        'vk_idx',
        client.c.vk, 
        postgresql_ops={
            'description': 'gin_trgm_ops',
        },
        postgresql_using='gin'
    )
    Index(
        'telegram_id_idx',
        client.c.telegram_id, 
        postgresql_ops={
            'description': 'gin_trgm_ops',
        },
        postgresql_using='gin'
    )
    Index(
        'instagram_idx',
        client.c.instagram, 
        postgresql_ops={
            'description': 'gin_trgm_ops',
        },
        postgresql_using='gin'
    )
    Index(
        'birthdate_idx',
        client.c.birthdate, 
        postgresql_ops={
            'description': 'gin_trgm_ops',
        },
        postgresql_using='gin'
    )
    Index(
        'phone_number_idx',
        client.c.phone_number, 
        postgresql_ops={
            'description': 'gin_trgm_ops',
        },
        postgresql_using='gin'
    )

    return client
