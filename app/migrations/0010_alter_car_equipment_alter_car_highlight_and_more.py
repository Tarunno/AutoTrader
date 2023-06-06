# Generated by Django 4.2 on 2023-06-05 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_car_body_style_alter_car_drivetrain_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='equipment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='highlight',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='known_flaw',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='modification',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='ownership_history',
            field=models.TextField(blank=True, null=True),
        ),
    ]