# Generated by Django 5.0.2 on 2024-02-26 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0009_reportcard_delete_ranks'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
