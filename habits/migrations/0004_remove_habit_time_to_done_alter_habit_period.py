# Generated by Django 5.1.2 on 2024-11-29 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_habit_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='time_to_done',
        ),
        migrations.AlterField(
            model_name='habit',
            name='period',
            field=models.CharField(blank=True, choices=[('day', 'Ежедневно'), ('week', 'Еженедельно')], max_length=4, null=True, verbose_name='Периодичность'),
        ),
    ]