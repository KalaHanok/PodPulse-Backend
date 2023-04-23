# Generated by Django 4.2 on 2023-04-23 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadAudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PodcastName', models.CharField(max_length=200)),
                ('SpeakerName', models.CharField(max_length=200)),
                ('PodcastDescription', models.TextField(max_length=500)),
                ('PodcastFile', models.FileField(upload_to='Aduio/')),
            ],
        ),
        migrations.CreateModel(
            name='UploadVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PodcastName', models.CharField(max_length=200)),
                ('SpeakerName', models.CharField(max_length=200)),
                ('PodcastDescription', models.TextField(max_length=500)),
                ('PodcastFile', models.FileField(upload_to='Vedios/')),
            ],
        ),
    ]