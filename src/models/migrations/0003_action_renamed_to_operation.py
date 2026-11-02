from tortoise import migrations
from tortoise.migrations import operations as ops


class Migration(migrations.Migration):
    dependencies = [("models", "0002_log_model")]

    initial = False

    operations = [
        ops.RenameField(
            model_name="Log",
            old_name="action",
            new_name="operation",
        ),
    ]
