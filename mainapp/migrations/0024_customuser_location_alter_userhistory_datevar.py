# Generated by Django 4.2.13 on 2024-09-27 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0023_rename_makecategory_item_categories_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='location',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userhistory',
            name='datevar',
            field=models.CharField(default='2024-09-27 19:27:41.640073', max_length=100),
        ),
    ]
