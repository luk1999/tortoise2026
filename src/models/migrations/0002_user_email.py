from tortoise import fields, migrations
from tortoise.migrations import operations as ops


class Migration(migrations.Migration):
    dependencies = [("models", "0001_initial")]

    initial = False

    operations = [
        ops.AddField(
            model_name="User",
            name="email",
            field=fields.CharField(unique=True, null=True, max_length=254),
        ),
    ]
