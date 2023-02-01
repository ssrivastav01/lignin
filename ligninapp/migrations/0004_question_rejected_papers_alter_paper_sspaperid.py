# Generated by Django 4.1.5 on 2023-02-01 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ligninapp', '0003_paper_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='rejected_papers',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='ssPaperID',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]