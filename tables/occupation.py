from sqlalchemy import Column, MetaData, Table, String

def create_table(metadata: MetaData) -> Table:
    occ = Table(
        'occupation',
        metadata,
        Column(
            'id',
            primary_key=True
        ),
        Column(
            'occupation',
            String(30),
            unique=True
        )
    )

    return occ
