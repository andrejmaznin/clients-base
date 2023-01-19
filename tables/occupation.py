from sqlalchemy import Column, MetaData, Table, String, Integer

def create_table(metadata: MetaData) -> Table:
    occ = Table(
        'occupation',
        metadata,
        Column(
            'id',
            Integer,
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
