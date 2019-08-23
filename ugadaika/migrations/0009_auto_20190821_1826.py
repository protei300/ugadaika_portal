# Generated by Django 2.2.4 on 2019-08-21 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ugadaika', '0008_endingfeature_materialfeature_sexfeature'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='ending_feature',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ugadaika.EndingFeature'),
        ),
        migrations.AddField(
            model_name='cards',
            name='material_feature',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ugadaika.MaterialFeature'),
        ),
        migrations.AddField(
            model_name='cards',
            name='sex_feature',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ugadaika.SexFeature'),
        ),
    ]
