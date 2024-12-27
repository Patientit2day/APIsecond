# Generated by Django 5.0.6 on 2024-11-04 10:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0017_rename_post_post_post_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_name',
            field=models.CharField(max_length=120),
        ),
    ]