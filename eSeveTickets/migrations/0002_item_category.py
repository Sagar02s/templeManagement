# Generated by Django 5.1.3 on 2024-11-06 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eSeveTickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
    ]