from sqlalchemy import Column, MetaData, Table, ForeignKey, Text


def create_table(metadata: MetaData) -> Table:
    auth_user = Table(
        'authuser',
        metadata,
        Column(
            'user',
            ForeignKey("user.id"),
            primary_key=True
        ),
        Column(
            'email',
            ForeignKey("user.email")
        ),
        Column(
            'phone_number',
            ForeignKey("user.phone_number")
        ),
        Column(
            'password_hash',
            Text
        )
    )

    return auth_user
