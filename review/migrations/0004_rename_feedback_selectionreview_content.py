# Generated by Django 5.1.1 on 2024-10-11 06:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("review", "0003_rename_reviewid_writingreview_id_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="selectionreview",
            old_name="feedback",
            new_name="content",
        ),
    ]