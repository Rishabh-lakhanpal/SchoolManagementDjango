# Generated by Django 4.1.3 on 2022-11-07 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stud',
            old_name='s_addr',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='stud',
            old_name='S_class',
            new_name='Classroom',
        ),
        migrations.RenameField(
            model_name='stud',
            old_name='s_email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='stud',
            old_name='s_name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='stud',
            old_name='s_school',
            new_name='School',
        ),
    ]