# Generated by Django 3.1.2 on 2021-02-27 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='provider',
            field=models.CharField(default='Internal', max_length=10),
        ),
    ]
