# Generated by Django 3.2 on 2022-08-29 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_delete_userdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='full_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
