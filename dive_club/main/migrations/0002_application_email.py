# Generated by Django 3.2.15 on 2025-02-20 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
    ]
