# Generated by Django 4.2.13 on 2024-07-25 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_alter_userhistory_datevar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userhistory',
            name='datevar',
            field=models.CharField(default='2024-07-26 01:03:07.949935', max_length=100),
        ),
    ]
