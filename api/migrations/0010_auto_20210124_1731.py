# Generated by Django 3.1.2 on 2021-01-24 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_recentchatcomments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='debate',
            name='CATEGORY_ID',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
