# Generated by Django 5.1.4 on 2024-12-15 17:04

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specifications', '0006_remove_requirement_spec_requirement_classification'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classification',
            options={'ordering': ['spec'], 'verbose_name_plural': 'classification'},
        ),
        migrations.AlterModelOptions(
            name='quality',
            options={'ordering': ['name'], 'verbose_name_plural': 'quality'},
        ),
        migrations.AlterModelOptions(
            name='requirement',
            options={'ordering': ['title'], 'verbose_name_plural': 'requirement'},
        ),
        migrations.AlterModelOptions(
            name='spec',
            options={'ordering': ['-title'], 'verbose_name_plural': 'spec'},
        ),
        migrations.CreateModel(
            name='Manual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manual_title', models.CharField(max_length=50)),
                ('manual_description', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manual_publish', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'manual process',
                'ordering': ['manual_title'],
                'indexes': [models.Index(fields=['manual_title'], name='specificati_manual__b840f3_idx')],
            },
        ),
        migrations.CreateModel(
            name='Method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=50)),
                ('process_identity', models.CharField(choices=[('CR', 'Chrome Plate'), ('NI', 'Nickel Plate'), ('CD', 'Cadmium Plate'), ('AN', 'Anodize'), ('CF', 'Chemical Converision'), ('PA', 'Passivation'), ('ST', 'Coating Strip'), ('BR', 'Brush Plate'), ('PR', 'Prepen Etch'), ('TE', 'Temper Etch')], default='N/A', max_length=50)),
                ('description', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='method_publish', to=settings.AUTH_USER_MODEL)),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='method_class', to='specifications.classification')),
            ],
            options={
                'verbose_name_plural': 'requirement',
                'ordering': ['title'],
                'indexes': [models.Index(fields=['title'], name='specificati_title_af42b6_idx')],
            },
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tank_identification', models.CharField(max_length=50)),
                ('tank_contents', models.CharField(max_length=200)),
                ('tank_size', models.CharField(help_text='Working Volume and Level', max_length=100)),
                ('temp_min', models.CharField(help_text=' Minium Temperature in F', max_length=50)),
                ('temp_max', models.CharField(help_text='Maximum Temperature in F', max_length=50)),
                ('time_min', models.CharField(help_text='Mininum Soak Time (minutes)', max_length=50)),
                ('time_max', models.CharField(help_text='Maximum Soak Time (minutes)', max_length=50)),
                ('tank_requirement', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tank_publish', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'tank process',
                'ordering': ['tank_identification'],
                'indexes': [models.Index(fields=['tank_identification'], name='specificati_tank_id_f583fa_idx')],
            },
        ),
    ]
