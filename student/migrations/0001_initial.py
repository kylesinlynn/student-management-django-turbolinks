# Generated by Django 4.0.3 on 2022-04-20 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('nrc', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('phone', models.CharField(max_length=20)),
                ('contact', models.CharField(choices=[('Yangon', 'Yangon'), ('Mandalay', 'Mandalay')], default=0, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtlid', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=4)),
                ('mark', models.IntegerField()),
                ('remark', models.TextField(max_length=280)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
