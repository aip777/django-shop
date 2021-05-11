# Generated by Django 3.2.2 on 2021-05-06 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25)),
                ('mobile', models.CharField(blank=True, max_length=18, null=True)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customer',
            },
        ),
    ]