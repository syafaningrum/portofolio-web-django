# Generated by Django 4.2.11 on 2024-05-05 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0005_alter_identity_born_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='education',
            name='start',
            field=models.DateField(),
        ),
    ]
