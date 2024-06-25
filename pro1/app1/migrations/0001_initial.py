# Generated by Django 5.0.6 on 2024-06-25 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=34)),
                ('last_name', models.CharField(max_length=34)),
                ('gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Others', 'others')], max_length=20)),
                ('profile_picture', models.ImageField(upload_to='profiles/')),
                ('Address', models.TextField()),
                ('City', models.CharField(max_length=34)),
            ],
        ),
    ]
