# Generated by Django 3.2.5 on 2021-07-27 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0014_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='department_id',
            field=models.IntegerField(null=True),
        ),
    ]
