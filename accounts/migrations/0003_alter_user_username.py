# Generated by Django 3.2 on 2022-02-03 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_auto_20220203_1633"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(blank=True, default=0, max_length=150, verbose_name="username"),
            preserve_default=False,
        ),
    ]
