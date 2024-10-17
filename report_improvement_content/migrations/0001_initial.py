# Generated by Django 5.1.1 on 2024-10-17 06:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('report_improvement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultReportImprovementContent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('improvement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='improvement_content', to='report_improvement.resultreportimprovement')),
            ],
            options={
                'db_table': 'report_improvement_content',
            },
        ),
    ]
