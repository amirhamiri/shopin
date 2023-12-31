# Generated by Django 5.0 on 2023-12-08 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="is_staff",),
        migrations.AddField(
            model_name="user",
            name="is_admin",
            field=models.BooleanField(default=False, verbose_name="Is admin"),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Is active"),
        ),
    ]
