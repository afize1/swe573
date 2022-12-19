# Generated by Django 3.1.1 on 2022-12-19 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_auto_20221218_2046'),
    ]

    operations = [
        migrations.CreateModel(
            name='postComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField()),
                ('username', models.CharField(max_length=20)),
                ('comment', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'db_post_comment',
            },
        ),
    ]
