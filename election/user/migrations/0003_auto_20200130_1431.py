# Generated by Django 3.0.2 on 2020-01-30 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200130_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='passport_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Passport Number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='permanent_block',
            field=models.IntegerField(blank=True, null=True, verbose_name='block number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='present_block',
            field=models.IntegerField(blank=True, null=True, verbose_name='block number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='present_ward',
            field=models.IntegerField(blank=True, null=True, verbose_name='ward number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='voting_booth',
            field=models.IntegerField(blank=True, null=True, verbose_name='booth number'),
        ),
    ]
