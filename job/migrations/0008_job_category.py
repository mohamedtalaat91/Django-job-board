# Generated by Django 5.0.7 on 2024-07-28 12:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_remove_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='job.category'),
            preserve_default=False,
        ),
    ]
