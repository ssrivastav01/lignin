# Generated by Django 4.1.5 on 2023-02-09 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ligninapp', '0006_value_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
