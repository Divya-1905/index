# Generated by Django 4.1.4 on 2022-12-27 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_groceroy_stateonery_alter_consumer_products_choice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('chocies', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=None, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Electronic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('items', models.CharField(choices=[('table', 'tabel'), ('chair', 'chair'), ('sofa', 'sofa')], default=None, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Furiniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('items', models.CharField(choices=[('table', 'tabel'), ('chair', 'chair'), ('sofa', 'sofa')], default=None, max_length=30, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='consumer',
            name='groceroy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.groceroy'),
        ),
        migrations.AddField(
            model_name='consumer',
            name='statenoery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.stateonery'),
        ),
        migrations.AddField(
            model_name='stateonery',
            name='items',
            field=models.CharField(choices=[('pen', 'pen'), ('books', 'books'), ('penclis', 'pencils')], default=None, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='stateonery',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='Products_choice',
            field=models.CharField(blank=True, choices=[('GROCEROY', 'groceroy'), ('STATENOERY', 'stateonery'), ('ELECTRONICS', 'electronics'), ('CLOTHING', 'clothing'), ('FURNITURE', 'furniture')], default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='groceroy',
            name='quanity',
            field=models.CharField(blank=True, choices=[('grams', 'grams'), ('kilograms', 'kilograms')], default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='consumer',
            name='clothing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.clothing'),
        ),
        migrations.AddField(
            model_name='consumer',
            name='electronic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.electronic'),
        ),
        migrations.AddField(
            model_name='consumer',
            name='furiniture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.furiniture'),
        ),
    ]
