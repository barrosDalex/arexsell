# Generated by Django 3.2.5 on 2021-07-12 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]