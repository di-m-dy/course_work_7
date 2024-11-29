# Generated by Django 5.1.2 on 2024-11-29 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='date_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата и время'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='period',
            field=models.CharField(blank=True, choices=[('day', 'Ежедневно'), ('week', 'Еженедельно')], default='day', max_length=4, null=True, verbose_name='Периодичность'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='time_to_done',
            field=models.TimeField(blank=True, null=True, verbose_name='Время на выполнение'),
        ),
    ]
