# Generated by Django 2.2.5 on 2019-09-20 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubbing', '0007_auto_20190921_0223'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='none.png', upload_to=''),
        ),
    ]
