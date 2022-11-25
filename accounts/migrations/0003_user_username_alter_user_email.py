# Generated by Django 4.0.2 on 2022-11-25 15:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_user_username_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=100, unique=True, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email address'),
        ),
    ]
