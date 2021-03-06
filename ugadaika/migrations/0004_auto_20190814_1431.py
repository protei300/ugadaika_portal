# Generated by Django 2.2.4 on 2019-08-14 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugadaika', '0003_remove_cards_sound'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardssoundsplace',
            old_name='card',
            new_name='cards',
        ),
        migrations.RenameField(
            model_name='cardssoundsplace',
            old_name='sound',
            new_name='sounds',
        ),
        migrations.AddField(
            model_name='cards',
            name='sound',
            field=models.ManyToManyField(through='ugadaika.CardsSoundsPlace', to='ugadaika.Sounds'),
        ),
    ]
