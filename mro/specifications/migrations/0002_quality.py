# Generated by Django 5.1.4 on 2024-12-15 02:02

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specifications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('methods', models.CharField(choices=[('LI', 'Lot Inspection'), ('PT', 'Periodic Test'), ('PRE', 'Preproduction Test')], max_length=3)),
                ('sample', models.CharField(choices=[('P', 'Part'), ('PL', 'Panel')], default='PL', max_length=3)),
                ('test_spec', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2)),
                ('spec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spec_quality', to='specifications.spec')),
            ],
            options={
                'ordering': ['name'],
                'indexes': [models.Index(fields=['name'], name='specificati_name_6034ec_idx')],
            },
        ),
    ]
