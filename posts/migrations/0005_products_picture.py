# Generated by Django 3.0.2 on 2020-03-23 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20200323_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
