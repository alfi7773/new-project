# Generated by Django 5.2 on 2025-05-04 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vmlr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pakets',
            name='price',
            field=models.CharField(default=1, max_length=100, verbose_name='цена'),
            preserve_default=False,
        ),
    ]
