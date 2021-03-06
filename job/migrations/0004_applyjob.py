# Generated by Django 3.1.6 on 2021-06-16 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applyjob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20, null=True)),
                ('lname', models.CharField(max_length=20, null=True)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=20, null=True)),
                ('experience', models.CharField(max_length=20, null=True)),
                ('qualification', models.CharField(max_length=20, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('num', models.IntegerField(null=True)),
            ],
        ),
    ]
