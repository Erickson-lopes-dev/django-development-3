# Generated by Django 3.0.8 on 2020-07-22 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_post_cetegories'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]
