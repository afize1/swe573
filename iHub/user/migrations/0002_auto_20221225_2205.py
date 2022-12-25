# Generated by Django 3.1.1 on 2022-12-25 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='followUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('followers', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'db_followers',
            },
        ),
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'db_table': 'db_images',
            },
        ),
        migrations.CreateModel(
            name='postComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField()),
                ('username', models.CharField(max_length=20)),
                ('comment', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'db_post_comment',
            },
        ),
        migrations.CreateModel(
            name='shares',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=255)),
                ('label', models.CharField(max_length=255)),
                ('private', models.CharField(max_length=20)),
                ('value', models.CharField(max_length=255)),
                ('comment', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'db_shares',
            },
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('security_question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='images/')),
                ('occupation', models.CharField(max_length=20)),
                ('interest', models.CharField(max_length=20)),
                ('bio', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'db_users',
            },
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]