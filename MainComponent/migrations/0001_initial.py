# Generated by Django 3.0.8 on 2020-09-14 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvaibleJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(default='', max_length=150)),
                ('description', models.TextField(default='')),
                ('requirements', models.TextField(default='')),
                ('one_day', models.TextField(default='')),
                ('released_day', models.DateTimeField(auto_now_add=True)),
                ('job_slug', models.SlugField(default='', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(default='', max_length=200, unique=True)),
                ('address', models.CharField(default='', max_length=200, unique=True)),
                ('country', models.CharField(choices=[('Romania', 'Romania')], default='Romania', max_length=100)),
                ('description', models.TextField(default='')),
                ('studio_slug', models.SlugField(default='', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobAppliance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=254)),
                ('years_of_experience', models.PositiveIntegerField(default=0)),
                ('curriculum_vitae', models.FileField(default='default.pdf', upload_to='curriculum_vitae/')),
                ('description_of_skills', models.TextField(default='')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('carrer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MainComponent.AvaibleJob')),
            ],
        ),
        migrations.AddField(
            model_name='avaiblejob',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MainComponent.Studio'),
        ),
    ]
