# Generated by Django 4.2.11 on 2024-03-21 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureToggle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('desc', models.CharField(max_length=200)),
                ('state', models.CharField(choices=[('enabled', 'Enabled'), ('disabled', 'Disabled')], max_length=20)),
                ('note', models.TextField()),
                ('env', models.CharField(max_length=20)),
                ('app', models.CharField(max_length=50)),
            ],
        ),
    ]
