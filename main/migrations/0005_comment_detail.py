# Generated by Django 3.2 on 2021-05-20 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_answer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='detail',
            field=models.TextField(default=''),
        ),
    ]
