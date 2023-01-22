from sqlalchemy import Column, MetaData, Table, String, text
from sqlalchemy.dialects.postgresql import UUID

def create_table(metadata: MetaData) -> Table:
    occ = Table(
        'occupation',
        metadata,
        Column(
            'id',
            UUID,
            server_default=text('gen_random_uuid()'),
            primary_key=True
        ),
        Column(
            'occupation',
            String(30),
            unique=True,
            index=True
        )
    )

    return occ
