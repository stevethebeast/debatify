# Generated by Django 3.1.2 on 2021-01-15 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210109_1624'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='argument_vote',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='counter_argument_vote',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='debate_vote',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='argument_vote',
            constraint=models.UniqueConstraint(fields=('ARGUMENT_ID', 'CONTACT_ID'), name='Unique Argument Vote'),
        ),
        migrations.AddConstraint(
            model_name='counter_argument_vote',
            constraint=models.UniqueConstraint(fields=('COUNTER_ARGUMENT_ID', 'CONTACT_ID'), name='Unique Counter Argument Vote'),
        ),
        migrations.AddConstraint(
            model_name='debate_vote',
            constraint=models.UniqueConstraint(fields=('DEBATE_ID', 'CONTACT_ID'), name='Unique Debate Vote'),
        ),
    ]
