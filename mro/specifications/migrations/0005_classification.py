# Generated by Django 5.1.4 on 2024-12-15 03:20

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specifications', '0004_requirement'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(default='N/A', max_length=50)),
                ('types', models.CharField(default='N/A', max_length=50)),
                ('classes', models.CharField(default='N/A', max_length=50)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classification_publish', to=settings.AUTH_USER_MODEL)),
                ('spec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spec_classification', to='specifications.spec')),
            ],
            options={
                'ordering': ['spec'],
                'indexes': [models.Index(fields=['spec'], name='specificati_spec_id_97f00d_idx')],
            },
        ),
    ]