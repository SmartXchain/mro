# Generated by Django 5.1.4 on 2024-12-14 23:19

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Spec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('revision', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('publisher', models.CharField(max_length=50)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spec_publish', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-title'],
                'indexes': [models.Index(fields=['-title'], name='specificati_title_09a47c_idx')],
            },
        ),
    ]
