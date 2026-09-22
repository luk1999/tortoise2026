from enums import Genre, UserStatus
from tortoise import fields, migrations
from tortoise.fields.base import OnDelete
from tortoise.migrations import operations as ops


class Migration(migrations.Migration):
    initial = True

    operations = [
        ops.CreateModel(
            name="Author",
            fields=[
                ("id", fields.IntField(generated=True, primary_key=True, unique=True, db_index=True)),
                ("first_name", fields.CharField(max_length=100)),
                ("last_name", fields.CharField(max_length=100)),
                ("date_of_birth", fields.DateField()),
            ],
            options={
                "table": "author",
                "app": "models",
                "unique_together": (("first_name", "last_name", "date_of_birth"),),
                "pk_attr": "id",
            },
            bases=["Model"],
        ),
        ops.CreateModel(
            name="Book",
            fields=[
                ("id", fields.IntField(generated=True, primary_key=True, unique=True, db_index=True)),
                (
                    "author",
                    fields.ForeignKeyField(
                        "models.Author",
                        source_field="author_id",
                        db_constraint=True,
                        to_field="id",
                        related_name="books",
                        on_delete=OnDelete.CASCADE,
                    ),
                ),
                ("title", fields.CharField(max_length=100)),
                ("year", fields.IntField()),
                (
                    "genre",
                    fields.CharEnumField(
                        description="adventure: adventure\nautobiography: autobiography\nbiography: biography\nfantasy: fantasy\nhistory: history\nhorror: horror\nmystery: mystery\npoetry: poetry\nromance: romance\nsci_fi: sci_fi\nthriller: thriller",
                        enum_type=Genre,
                        max_length=13,
                    ),
                ),
            ],
            options={"table": "book", "app": "models", "unique_together": (("author", "title"),), "pk_attr": "id"},
            bases=["Model"],
        ),
        ops.CreateModel(
            name="User",
            fields=[
                ("id", fields.IntField(generated=True, primary_key=True, unique=True, db_index=True)),
                ("username", fields.CharField(unique=True, max_length=50)),
                ("password", fields.CharField(max_length=32)),
                ("first_name", fields.CharField(null=True, max_length=100)),
                ("last_name", fields.CharField(null=True, max_length=100)),
                (
                    "status",
                    fields.CharEnumField(
                        default=UserStatus.INACTIVE,
                        description="INACTIVE: inactive\nACTIVE: active\nDELETED: deleted",
                        enum_type=UserStatus,
                        max_length=8,
                    ),
                ),
                (
                    "books",
                    fields.ManyToManyField(
                        "models.Book",
                        unique=True,
                        db_constraint=True,
                        through="user_book",
                        forward_key="book_id",
                        backward_key="user_id",
                        related_name="users",
                        on_delete=OnDelete.CASCADE,
                    ),
                ),
            ],
            options={"table": "user", "app": "models", "pk_attr": "id"},
            bases=["Model"],
        ),
    ]
