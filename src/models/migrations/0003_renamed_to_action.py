from tortoise import migrations
from tortoise.migrations import operations as ops


class Migration(migrations.Migration):
    dependencies = [("models", "0002_log_model")]

    initial = False

    operations = [
        ops.RenameModel(old_name="Log", new_name="Action"),
    ]
