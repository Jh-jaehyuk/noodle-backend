# Generated by Django 5.1.1 on 2024-09-23 03:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("survey", "0002_surveyquestion_surveyquestionsentence_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="surveyquestion",
            name="SurveyQuestionSentence",
            field=models.CharField(default=None, max_length=500),
        ),
    ]