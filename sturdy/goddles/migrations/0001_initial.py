# Generated by Django 4.2.9 on 2024-02-12 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('total_score', models.DecimalField(decimal_places=1, max_digits=5)),
                ('chinese_score', models.DecimalField(decimal_places=1, max_digits=5)),
                ('math_score', models.DecimalField(decimal_places=1, max_digits=5)),
                ('english_score', models.DecimalField(decimal_places=1, max_digits=5)),
                ('physics_score', models.DecimalField(decimal_places=1, max_digits=5)),
                ('average_score', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]