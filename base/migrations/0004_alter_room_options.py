# Generated by Django 5.0.1 on 2024-02-13 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_messgae_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
