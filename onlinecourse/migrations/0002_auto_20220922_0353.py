# Generated by Django 3.1.3 on 2022-09-22 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=35)),
                ('is_correct', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choices', models.ManyToManyField(to='onlinecourse.Choice')),
                ('enrollment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.enrollment')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gradePoint', models.IntegerField(default=2)),
                ('questionContent', models.CharField(max_length=35)),
                ('course', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.course')),
                ('lesson_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.lesson')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.question'),
        ),
    ]
