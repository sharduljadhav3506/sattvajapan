# Generated by Django 4.2.13 on 2024-09-13 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_alter_item_availablequantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='availablequantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userhistory',
            name='datevar',
            field=models.CharField(default='2024-09-13 19:27:55.666206', max_length=100),
        ),
    ]
