# Generated by Django 4.2.5 on 2023-10-16 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_post_slug_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(limit_choices_to={'parent_tag__isnull': True}, max_length=2, to='core.tag'),
        ),
    ]
