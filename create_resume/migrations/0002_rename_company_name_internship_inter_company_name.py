# Generated by Django 3.2.4 on 2021-10-16 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create_resume', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='internship',
            old_name='company_name',
            new_name='inter_company_name',
        ),
    ]