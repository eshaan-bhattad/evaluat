# Generated by Django 3.2 on 2021-04-09 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluatapp', '0003_auto_20210409_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='evaluations_given',
            field=models.ManyToManyField(blank=True, related_name='evaluatee_evaluator', to='evaluatapp.Evaluation'),
        ),
        migrations.AlterField(
            model_name='user',
            name='evaluations_received',
            field=models.ManyToManyField(blank=True, related_name='evaluator_evaluatee', to='evaluatapp.Evaluation'),
        ),
    ]
