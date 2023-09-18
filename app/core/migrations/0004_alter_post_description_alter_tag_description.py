# Generated by Django 4.2.5 on 2023-09-12 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_tag_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(default='This post has no description yet!', max_length=250),
        ),
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.TextField(default='This tag has no description yet!', max_length=300),
        ),
    ]
