# Generated by Django 3.0.3 on 2020-10-26 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=256)),
                ('subject', models.CharField(max_length=256)),
                ('message', models.CharField(max_length=2000)),
                ('file', models.FileField(upload_to='files')),
            ],
        ),
    ]
