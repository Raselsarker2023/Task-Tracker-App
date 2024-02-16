# Generated by Django 5.0 on 2024-02-16 14:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Schedule', '__first__'),
        ('projects', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.CharField(blank=True, max_length=15, null=True)),
                ('projects', models.ManyToManyField(blank=True, related_name='user_accounts', to='projects.projectmodel')),
                ('schedules', models.ManyToManyField(blank=True, related_name='user_accounts', to='Schedule.schedulemodel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
