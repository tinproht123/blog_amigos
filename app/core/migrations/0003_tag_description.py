# Generated by Django 4.2.5 on 2023-09-12 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post_created_at_remove_post_tag_post_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='description',
            field=models.CharField(default='This tag has no description yet!', max_length=250),
        ),
    ]
