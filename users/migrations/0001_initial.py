# Generated by Django 4.1.3 on 2022-11-06 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=30)),
                ('S_class', models.CharField(max_length=30)),
                ('s_addr', models.CharField(max_length=30)),
                ('s_school', models.CharField(max_length=30)),
                ('s_email', models.EmailField(max_length=30)),
            ],
        ),
    ]
