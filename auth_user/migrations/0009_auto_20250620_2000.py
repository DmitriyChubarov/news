# Generated by Django 2.2.5 on 2025-06-20 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0008_auto_20250514_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
