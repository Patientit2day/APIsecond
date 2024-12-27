# Generated by Django 5.0.6 on 2024-11-03 10:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0004_employe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('surname', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=12)),
                ('title', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('contrat', models.FileField(upload_to='pdf_contrats/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('surname', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=12)),
                ('title', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('salary', models.CharField(max_length=255)),
                ('post', models.CharField(max_length=255)),
                ('adress', models.CharField(max_length=255)),
                ('typecontrat', models.CharField(max_length=255)),
                ('contrat', models.FileField(upload_to='pdf_contrats/')),
                ('hiring_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('surname', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=12)),
                ('title', models.CharField(max_length=255)),
                ('contrat', models.FileField(blank=True, null=True, upload_to='pdf_contrats/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('adress', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
                ('pdftitle', models.CharField(max_length=255)),
                ('pdfid', models.FileField(blank=True, null=True, upload_to='pdf_contrats/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='Employe',
        ),
    ]
