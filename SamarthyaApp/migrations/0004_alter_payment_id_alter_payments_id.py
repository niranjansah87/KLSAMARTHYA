# Generated by Django 4.0.6 on 2023-02-22 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SamarthyaApp', '0003_auto_20230222_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]