# Generated by Django 2.1.5 on 2019-03-01 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='posts_count',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
