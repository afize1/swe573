# Generated by Django 4.1.3 on 2022-11-27 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0021_shares"),
    ]

    operations = [
        migrations.CreateModel(
            name="followUser",
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
                ("followers", models.CharField(max_length=20)),
            ],
            options={"db_table": "db_followers",},
        ),
    ]