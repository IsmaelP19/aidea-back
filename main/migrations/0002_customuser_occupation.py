# Generated by Django 5.0.7 on 2024-07-17 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='occupation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
