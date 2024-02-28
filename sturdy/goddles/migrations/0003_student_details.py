# Generated by Django 4.2.9 on 2024-02-27 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goddles', '0002_student_school'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=50)),
                ('class_number', models.IntegerField()),
                ('total_score', models.DecimalField(decimal_places=1, max_digits=5)),
                ('class_average_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('school_average_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('district_average_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('chinese_score', models.DecimalField(decimal_places=1, max_digits=5)),
                ('class_chinese_average_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('school_chinese_average_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('district_chinese_average_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('math_score', models.DecimalField(decimal_places=1, max_digits=5)),
                ('class_math_average_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('school_math_average_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('district_math_average_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('english_score', models.DecimalField(decimal_places=1, max_digits=5)),
                ('class_english_average_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('school_english_average_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('district_english_average_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('physics_score', models.DecimalField(decimal_places=1, max_digits=5)),
                ('class_physics_average_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('school_physics_average_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('district_physics_average_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('history_score_one', models.DecimalField(decimal_places=1, max_digits=5)),
                ('history_chinese_score_one', models.DecimalField(decimal_places=1, max_digits=5)),
                ('history_math_score_one', models.DecimalField(decimal_places=1, max_digits=5)),
                ('history_english_score_one', models.DecimalField(decimal_places=1, max_digits=5)),
                ('history_score_two', models.DecimalField(decimal_places=1, max_digits=5)),
                ('history_chinese_score_two', models.DecimalField(decimal_places=1, max_digits=5)),
                ('history_math_score_two', models.DecimalField(decimal_places=1, max_digits=5)),
                ('history_english_score_two', models.DecimalField(decimal_places=1, max_digits=5)),
            ],
        ),
    ]