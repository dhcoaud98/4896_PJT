# Generated by Django 3.2.2 on 2022-05-23 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_review_movie_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='movie_id',
            new_name='movie',
        ),
    ]