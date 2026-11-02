from tortoise import migrations
from tortoise.migrations import operations as ops
from enums import UserAction
from tortoise import fields


class Migration(migrations.Migration):
    dependencies = [("models", "0002_log_model")]

    initial = False

    operations = [
        ops.AlterField(
            model_name="Login",
            name="action",
            field=fields.CharEnumField(
                description="LOGIN: login\nLOGOUT: logout",
                enum_type=UserAction,
                max_length=50,
            ),
        ),
    ]
