# Generated by Django 4.1.3 on 2022-11-12 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0002_alter_cook_years_of_experience"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cook",
            name="years_of_experience",
            field=models.IntegerField(default=0, null=True),
        ),
    ]