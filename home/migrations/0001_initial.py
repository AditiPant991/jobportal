# Generated by Django 3.2.4 on 2021-10-14 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply_for_job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('start_date', models.CharField(max_length=200)),
                ('job_type', models.CharField(max_length=50)),
                ('package', models.CharField(max_length=200)),
                ('apply_by', models.CharField(max_length=200)),
                ('applied_by', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('start_date', models.CharField(max_length=200)),
                ('job_type', models.CharField(choices=[('', 'Choose job-type:'), ('Internship', 'Internship'), ('Part-Time', 'Part-Time'), ('Full-time', 'Full-time')], max_length=50)),
                ('package', models.CharField(max_length=200)),
                ('apply_by', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200, null=True)),
                ('about_company', models.TextField(max_length=1500)),
                ('job_description', models.TextField(max_length=1500)),
                ('eligibility', models.TextField(max_length=500)),
                ('perks', models.TextField(max_length=500)),
                ('openings', models.IntegerField()),
                ('is_applied', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('mobile', models.CharField(default='+91', max_length=13)),
                ('resume', models.FileField(null=True, upload_to='resume/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recieve_job_applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200, null=True)),
                ('applied_by', models.CharField(max_length=200, null=True)),
                ('resume_file', models.FileField(null=True, upload_to='')),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('job_created_by', models.CharField(max_length=200, null=True)),
                ('apply_for_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.apply_for_job')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.job')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.resume')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='apply_for_job',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.job'),
        ),
        migrations.AddField(
            model_name='apply_for_job',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.resume'),
        ),
        migrations.AddField(
            model_name='apply_for_job',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
