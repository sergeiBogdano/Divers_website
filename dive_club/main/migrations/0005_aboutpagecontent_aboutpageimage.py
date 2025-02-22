# Generated by Django 3.2.15 on 2025-02-21 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_homepagecontent_homepageimage_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AboutPageImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about_images/')),
                ('caption', models.CharField(blank=True, max_length=200)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.aboutpagecontent')),
            ],
        ),
    ]
