# Generated by Django 3.0.8 on 2020-07-22 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_post_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]
