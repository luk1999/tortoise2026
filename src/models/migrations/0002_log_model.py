from tortoise import migrations
from tortoise.migrations import operations as ops
from tortoise import fields


class Migration(migrations.Migration):
    dependencies = [("models", "0001_initial")]

    initial = False

    operations = [
        ops.CreateModel(
            name="Log",
            fields=[
                ("id", fields.IntField(generated=True, primary_key=True, unique=True, db_index=True)),
                ("action", fields.CharField(max_length=50)),
                ("message", fields.TextField(null=True, unique=False)),
                ("created_at", fields.DatetimeField(auto_now=False, auto_now_add=True)),
            ],
            options={"table": "log", "app": "models", "pk_attr": "id"},
            bases=["Model"],
        ),
    ]
