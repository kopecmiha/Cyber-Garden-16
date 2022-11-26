# Generated by Django 4.0.2 on 2022-11-25 19:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("department", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="department",
            name="members",
            field=models.ManyToManyField(
                blank=True,
                related_name="department_members",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
