# Generated by Django 3.2 on 2021-04-09 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('linkedin', models.CharField(max_length=100)),
                ('github', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('githubRepo', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='evaluatapp.user')),
                ('students', models.ManyToManyField(related_name='user_groups', to='evaluatapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountability', models.IntegerField(default=0)),
                ('commitment', models.PositiveIntegerField(default=0)),
                ('conflict', models.PositiveIntegerField(default=0)),
                ('trust', models.PositiveIntegerField(default=0)),
                ('comments', models.TextField(max_length=1000)),
                ('evaluatee', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='evaluatee', to='evaluatapp.user')),
                ('evaluator', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='evaluator', to='evaluatapp.user')),
            ],
        ),
    ]