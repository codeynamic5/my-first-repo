# Generated by Django 5.1 on 2024-09-11 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_moodentry_mood_alter_moodentry_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='moodentry',
            name='mood',
            field=models.CharField(default='', max_length=255),
        ),
    ]
