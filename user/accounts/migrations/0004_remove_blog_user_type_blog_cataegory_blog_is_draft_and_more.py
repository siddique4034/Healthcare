# Generated by Django 5.0.7 on 2024-07-19 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_blog_user_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="user_type",
        ),
        migrations.AddField(
            model_name="blog",
            name="cataegory",
            field=models.CharField(
                choices=[
                    ("Immunization", "Immunization"),
                    ("Mental health", "mental_health"),
                    ("Covid 19", "covid_19"),
                    ("Heart disease", "heart_disease"),
                ],
                default="Immunization",
                max_length=13,
            ),
        ),
        migrations.AddField(
            model_name="blog",
            name="is_draft",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="blog",
            name="content",
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="blog",
            name="summary",
            field=models.TextField(max_length=200),
        ),
    ]
