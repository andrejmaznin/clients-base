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
            'firstname',
            ForeignKey('user.firstname')
        ),
        Column(
            'lastname',
            ForeignKey('user.lastname')
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
        'user_idx',
        client.c.user, postgresql_using='gin',
        postgresql_ops={
            'description': 'gin_trgm_ops',
        }
    )
    Index(
        'firstname_idx',
        client.c.firstname, postgresql_using='gin',
        postgresql_ops={
            'description': 'gin_trgm_ops',
        }
    )
    Index(
        'lastname_idx',
        client.c.lastname, postgresql_using='gin',
        postgresql_ops={
            'description': 'gin_trgm_ops',
        }
    )
    Index(
        'occupation_idx',
        client.c.occupation, postgresql_using='gin',
        postgresql_ops={
            'description': 'gin_trgm_ops',
        }
    )
    Index(
        'work_place_idx',
        client.c.work_place, postgresql_using='gin',
        postgresql_ops={
            'description': 'gin_trgm_ops',
        }
    )
    Index(
        'imgs_idx',
        client.c.imgs, postgresql_using='gin',
        postgresql_ops={
            'description': 'gin_trgm_ops',
        }
    )
    Index(
        'email_idx',
        client.c.email, postgresql_using='gin',
        postgresql_ops={
            'description': 'gin_trgm_ops',
        }
    )

    return client
