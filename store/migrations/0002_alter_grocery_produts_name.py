# Generated by Django 4.1.4 on 2022-12-28 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocery',
            name='produts_name',
            field=models.CharField(choices=[('sugar', 'sugar'), ('chocolate', 'chocolate')], default=None, max_length=30, null=True),
        ),
    ]