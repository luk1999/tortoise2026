from tortoise import migrations

EMAILS = {
    "john_smith": "john_smith@example.com",
    "rambo": "rambo@coba.de",
}


async def forwards(apps, schema_editor):
    """ Set emails for existing users """
    User = apps.get_model("models", "User")
    for username, email in EMAILS.items():
        user = await User.get(username__iexact=username)
        user.email = email
        await user.save()


async def backwards(apps, schema_editor):
    """ Removes emails """
    User = apps.get_model("models", "User")
    await User.filter(username__in=EMAILS).update(email=None)


class Migration(migrations.Migration):
    dependencies = [
        ("models", "0002_user_email"),
    ]

    initial = False

    operations = [migrations.RunPython(code=forwards, reverse_code=backwards)]
