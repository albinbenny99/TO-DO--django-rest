# Generated by Django 5.0.1 on 2024-02-01 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField(blank=True)),
                ('Date', models.DateField()),
                ('Completed', models.BooleanField(default=False)),
            ],
        ),
    ]
