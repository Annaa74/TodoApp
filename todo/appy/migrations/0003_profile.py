# Generated by Django 5.0.7 on 2024-07-27 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appy', '0002_todo_is_completed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('profile_pic', models.ImageField(upload_to='profile_pic/')),
            ],
        ),
    ]
