# Generated by Django 3.1.2 on 2021-01-24 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210124_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='debate',
            name='CATEGORY_ID',
            field=models.IntegerField(default=1),
        ),
    ]
