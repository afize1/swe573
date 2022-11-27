# Generated by Django 4.1.3 on 2022-11-27 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0020_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="shares",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=20)),
                ("subject", models.CharField(max_length=20)),
                ("label", models.CharField(max_length=20)),
                ("private", models.CharField(max_length=20)),
                ("type", models.CharField(max_length=20)),
                ("related_subjects", models.CharField(max_length=20)),
                ("value", models.CharField(max_length=20)),
                ("comment", models.CharField(max_length=20)),
            ],
            options={"db_table": "db_shares",},
        ),
    ]