# Generated by Django 3.2.7 on 2021-10-01 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['title']},
        ),
        migrations.AlterField(
            model_name='page',
            name='content',
            field=models.TextField(),
        ),
    ]