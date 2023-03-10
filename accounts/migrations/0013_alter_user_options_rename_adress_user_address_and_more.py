# Generated by Django 4.1.4 on 2022-12-26 09:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_user_password'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['created_at']},
        ),
        migrations.RenameField(
            model_name='user',
            old_name='adress',
            new_name='address',
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
