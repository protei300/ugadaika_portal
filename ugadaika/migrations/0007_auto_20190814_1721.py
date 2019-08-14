# Generated by Django 2.2.4 on 2019-08-14 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ugadaika', '0006_auto_20190814_1650'),
    ]
    atomic = False
    operations = [
        migrations.CreateModel(
            name='ColorFeature',
            fields=[
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('color_name', models.CharField(db_column='Цвет', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ShapeFeature',
            fields=[
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('shape_name', models.CharField(db_column='Форма', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SlogFeature',
            fields=[
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('slog_name', models.CharField(db_column='Слоги', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SuffixFeature',
            fields=[
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('suffix_name', models.CharField(db_column='Суффикс', max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='Sounds',
            new_name='SoundsFeature',
        ),
        migrations.AddField(
            model_name='cards',
            name='color_feature',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ugadaika.ColorFeature'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cards',
            name='shape_feature',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ugadaika.ShapeFeature'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cards',
            name='slog_feature',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ugadaika.SlogFeature'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cards',
            name='suffix_feature',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ugadaika.SuffixFeature'),
            preserve_default=False,
        ),
    ]