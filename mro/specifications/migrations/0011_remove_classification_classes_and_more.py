# Generated by Django 5.1.4 on 2024-12-15 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specifications', '0010_remove_solution_temp_max_remove_solution_temp_min_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classification',
            name='classes',
        ),
        migrations.RemoveField(
            model_name='classification',
            name='method',
        ),
        migrations.RemoveField(
            model_name='classification',
            name='types',
        ),
        migrations.AddField(
            model_name='classification',
            name='classificiation',
            field=models.CharField(default='N/A', help_text='Combination of methods, types, and classes. Use only one per process', max_length=200),
        ),
        migrations.AddField(
            model_name='classification',
            name='description',
            field=models.TextField(blank=True, help_text='description of method, type, or class'),
        ),
        migrations.AlterField(
            model_name='manual',
            name='manual_description',
            field=models.TextField(help_text='Small description of task to be performed'),
        ),
    ]
