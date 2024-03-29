# Generated by Django 4.2.9 on 2024-03-06 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goddles', '0004_student_evaluate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chinese',
            fields=[
                ('exam_number', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('school', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('class_number', models.IntegerField()),
                ('score', models.FloatField()),
                ('obj_answer', models.CharField(max_length=50)),
                ('q_064651', models.IntegerField()),
                ('q_141359', models.IntegerField()),
                ('q_167456', models.IntegerField()),
                ('q_220142', models.IntegerField()),
                ('q_411762', models.IntegerField()),
                ('q_579264', models.IntegerField()),
                ('q_595197', models.IntegerField()),
                ('q_706965', models.IntegerField()),
                ('q_714471', models.IntegerField()),
                ('q_859813', models.IntegerField()),
                ('q_922976', models.IntegerField()),
                ('analysis_synthesis_score_rate', models.CharField(max_length=10)),
                ('q_135664', models.IntegerField()),
                ('q_143861', models.IntegerField()),
                ('q_184697', models.IntegerField()),
                ('q_398892', models.IntegerField()),
                ('q_477885', models.IntegerField()),
                ('q_628680', models.IntegerField()),
                ('q_675002', models.IntegerField()),
                ('q_826748', models.IntegerField()),
                ('q_828333', models.IntegerField()),
                ('memorization_score_rate', models.CharField(max_length=10)),
                ('q_176499', models.IntegerField()),
                ('q_222350', models.IntegerField()),
                ('q_706277', models.IntegerField()),
                ('understanding_score_rate', models.CharField(max_length=10)),
                ('q_411515', models.IntegerField()),
                ('q_892131', models.IntegerField()),
                ('q_909416', models.IntegerField()),
                ('evaluation_appreciation_score_rate', models.CharField(max_length=10)),
                ('q_449977', models.IntegerField()),
                ('q_536461', models.IntegerField()),
                ('q_696435', models.IntegerField()),
                ('q_700448', models.IntegerField()),
                ('expression_application_score_rate', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='English',
            fields=[
                ('exam_number', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('school', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('class_number', models.IntegerField()),
                ('score', models.FloatField()),
                ('obj_answer', models.CharField(max_length=50)),
                ('q_023054', models.IntegerField()),
                ('q_041199', models.IntegerField()),
                ('q_121944', models.IntegerField()),
                ('q_373906', models.IntegerField()),
                ('q_545482', models.IntegerField()),
                ('q_783124', models.IntegerField()),
                ('q_885796', models.IntegerField()),
                ('q_581112', models.IntegerField()),
                ('q_646592', models.IntegerField()),
                ('application_score_rate', models.CharField(max_length=10)),
                ('q_046599', models.IntegerField()),
                ('q_056222', models.IntegerField()),
                ('q_058097', models.IntegerField()),
                ('q_066434', models.IntegerField()),
                ('q_080338', models.IntegerField()),
                ('q_089917', models.IntegerField()),
                ('q_119656', models.IntegerField()),
                ('q_119940', models.IntegerField()),
                ('q_123892', models.IntegerField()),
                ('q_145940', models.IntegerField()),
                ('q_155587', models.IntegerField()),
                ('q_160805', models.IntegerField()),
                ('q_181567', models.IntegerField()),
                ('q_189163', models.IntegerField()),
                ('q_216622', models.IntegerField()),
                ('q_258322', models.IntegerField()),
                ('q_278814', models.IntegerField()),
                ('q_291806', models.IntegerField()),
                ('q_331950', models.IntegerField()),
                ('q_337547', models.IntegerField()),
                ('q_337641', models.IntegerField()),
                ('q_443577', models.IntegerField()),
                ('q_468988', models.IntegerField()),
                ('q_497901', models.IntegerField()),
                ('q_516905', models.IntegerField()),
                ('q_518132', models.IntegerField()),
                ('q_528221', models.IntegerField()),
                ('q_542136', models.IntegerField()),
                ('q_563161', models.IntegerField()),
                ('q_571646', models.IntegerField()),
                ('q_578392', models.IntegerField()),
                ('q_597057', models.IntegerField()),
                ('q_610251', models.IntegerField()),
                ('q_611913', models.IntegerField()),
                ('q_620962', models.IntegerField()),
                ('q_633675', models.IntegerField()),
                ('q_636420', models.IntegerField()),
                ('q_648545', models.IntegerField()),
                ('q_655166', models.IntegerField()),
                ('q_668499', models.IntegerField()),
                ('q_691201', models.IntegerField()),
                ('q_703583', models.IntegerField()),
                ('q_723773', models.IntegerField()),
                ('q_751119', models.IntegerField()),
                ('q_762352', models.IntegerField()),
                ('q_767333', models.IntegerField()),
                ('q_768591', models.IntegerField()),
                ('q_782627', models.IntegerField()),
                ('q_782806', models.IntegerField()),
                ('q_786382', models.IntegerField()),
                ('q_811220', models.IntegerField()),
                ('q_817779', models.IntegerField()),
                ('q_826590', models.IntegerField()),
                ('q_868280', models.IntegerField()),
                ('q_868946', models.IntegerField()),
                ('q_872664', models.IntegerField()),
                ('q_920702', models.IntegerField()),
                ('q_958036', models.IntegerField()),
                ('q_972781', models.IntegerField()),
                ('q_984100', models.IntegerField()),
                ('q_992120', models.IntegerField()),
                ('q_992857', models.IntegerField()),
                ('comprehension_score_rate', models.CharField(max_length=10)),
                ('q_312704', models.IntegerField()),
                ('q_439330', models.IntegerField()),
                ('q_495719', models.IntegerField()),
                ('q_574420', models.IntegerField()),
                ('q_598148', models.IntegerField()),
                ('q_667318', models.IntegerField()),
                ('q_753433', models.IntegerField()),
                ('q_807038', models.IntegerField()),
                ('q_958308', models.IntegerField()),
                ('q_964789', models.IntegerField()),
                ('memorization_score_rate', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Math',
            fields=[
                ('exam_number', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('school', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('class_number', models.IntegerField()),
                ('score', models.FloatField()),
                ('obj_answer', models.CharField(max_length=50)),
                ('q_081615', models.IntegerField()),
                ('q_171561', models.IntegerField()),
                ('q_556513', models.IntegerField()),
                ('q_769263', models.IntegerField()),
                ('q_817009', models.IntegerField()),
                ('q_867590', models.IntegerField()),
                ('understanding_score_rate', models.CharField(max_length=10)),
                ('q_108408', models.IntegerField()),
                ('q_164172', models.IntegerField()),
                ('q_261944', models.IntegerField()),
                ('q_326328', models.IntegerField()),
                ('q_615029', models.IntegerField()),
                ('q_739564', models.IntegerField()),
                ('q_950394', models.IntegerField()),
                ('q_978943', models.IntegerField()),
                ('mastery_score_rate', models.CharField(max_length=10)),
                ('q_124251', models.IntegerField()),
                ('q_135164', models.IntegerField()),
                ('q_153565', models.IntegerField()),
                ('q_304364', models.IntegerField()),
                ('q_310458', models.IntegerField()),
                ('q_573602', models.IntegerField()),
                ('q_592845', models.IntegerField()),
                ('comprehension_score_rate', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Physics',
            fields=[
                ('exam_number', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('school', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('class_number', models.IntegerField()),
                ('score', models.FloatField()),
                ('obj_answer', models.CharField(max_length=50)),
                ('q_002200', models.IntegerField()),
                ('q_058585', models.IntegerField()),
                ('q_079084', models.IntegerField()),
                ('q_163397', models.IntegerField()),
                ('q_178041', models.IntegerField()),
                ('q_237720', models.IntegerField()),
                ('q_318738', models.IntegerField()),
                ('q_383693', models.IntegerField()),
                ('q_411179', models.IntegerField()),
                ('q_419032', models.IntegerField()),
                ('q_487965', models.IntegerField()),
                ('q_517582', models.IntegerField()),
                ('q_650534', models.IntegerField()),
                ('q_730097', models.IntegerField()),
                ('q_775828', models.IntegerField()),
                ('q_790477', models.IntegerField()),
                ('q_795744', models.IntegerField()),
                ('q_909969', models.IntegerField()),
                ('q_918334', models.IntegerField()),
                ('comprehension_score_rate', models.CharField(max_length=10)),
                ('q_124781', models.IntegerField()),
                ('q_129005', models.IntegerField()),
                ('q_250939', models.IntegerField()),
                ('q_275932', models.IntegerField()),
                ('q_322481', models.IntegerField()),
                ('q_467043', models.IntegerField()),
                ('q_550369', models.IntegerField()),
                ('q_556341', models.IntegerField()),
                ('q_800612', models.IntegerField()),
                ('q_827409', models.IntegerField()),
                ('q_994495', models.IntegerField()),
                ('recognition_score_rate', models.CharField(max_length=10)),
            ],
        ),
    ]
