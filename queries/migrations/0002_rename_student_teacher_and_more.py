# Generated by Django 4.1.7 on 2023-03-14 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("queries", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Student",
            new_name="Teacher",
        ),
        migrations.RenameField(
            model_name="teacher",
            old_name="first_name",
            new_name="firstname",
        ),
        migrations.RenameField(
            model_name="teacher",
            old_name="last_name",
            new_name="lastname",
        ),
    ]
