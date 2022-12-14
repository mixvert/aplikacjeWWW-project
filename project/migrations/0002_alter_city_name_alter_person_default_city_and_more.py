# Generated by Django 4.1.4 on 2022-12-12 18:25

from django.db import migrations, models
import project.models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=25, validators=[project.models.LettersOnlyValidator, project.models.FirstLetterValidator]),
        ),
        migrations.AlterField(
            model_name='person',
            name='default_city',
            field=models.CharField(default='New York', max_length=25, validators=[project.models.LettersOnlyValidator, project.models.FirstLetterValidator]),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=25, validators=[project.models.LettersOnlyValidator, project.models.FirstLetterValidator]),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=25, validators=[project.models.LettersOnlyValidator, project.models.FirstLetterValidator]),
        ),
    ]
