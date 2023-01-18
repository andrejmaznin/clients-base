from sqlalchemy import Column, text, MetaData, Table, String, Boolean, DATE, ForeignKey, Index
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
            'work_place',
            String(30)
        ),
        Column(
            'income',
            String(30)
        ),
        Column(
            'imgs',
            JSONB
        ),
        Column(
            'phone_number',
            ForeignKey('user.phone_number')
        ),
        Column(
            'email',
            ForeignKey('user.email')
        ),
        Column(
            'telegram_id',
            String(30)
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

    return client
