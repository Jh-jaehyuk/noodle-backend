# Generated by Django 5.1.1 on 2024-10-11 06:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("review", "0002_reviewlist_selectionreview_writingreview_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="writingreview",
            old_name="reviewId",
            new_name="id",
        ),
        migrations.AlterField(
            model_name="selectionreview",
            name="design",
            field=models.IntegerField(
                choices=[(1, "ONE"), (2, "TWO"), (3, "THREE"), (4, "FOUR"), (5, "FIVE")]
            ),
        ),
        migrations.AlterField(
            model_name="selectionreview",
            name="quality",
            field=models.IntegerField(
                choices=[(1, "ONE"), (2, "TWO"), (3, "THREE"), (4, "FOUR"), (5, "FIVE")]
            ),
        ),
        migrations.AlterField(
            model_name="selectionreview",
            name="speed",
            field=models.IntegerField(
                choices=[(1, "ONE"), (2, "TWO"), (3, "THREE"), (4, "FOUR"), (5, "FIVE")]
            ),
        ),
        migrations.AlterField(
            model_name="selectionreview",
            name="using",
            field=models.IntegerField(
                choices=[(1, "ONE"), (2, "TWO"), (3, "THREE"), (4, "FOUR"), (5, "FIVE")]
            ),
        ),
    ]