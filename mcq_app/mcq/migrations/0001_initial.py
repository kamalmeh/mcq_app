# Generated by Django 2.2.6 on 2019-11-20 16:46

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(blank=True, max_length=250, null=True, unique=True, verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.TextField()),
                ('Answer', models.CharField(max_length=255)),
                ('Options', models.TextField()),
                ('Weight', models.IntegerField(default=1, null=True)),
                ('Category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mcq.Category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Test_Name', models.CharField(default='Provide Test Name', max_length=255)),
                ('Category_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mcq.Category')),
            ],
            options={
                'verbose_name': 'Test',
                'verbose_name_plural': 'Tests',
            },
        ),
        migrations.CreateModel(
            name='TestQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mcq.Test')),
                ('test_Question', models.ForeignKey(on_delete=django.db.models.expressions.Case, to='mcq.Question')),
            ],
            options={
                'verbose_name': 'TestQuestion',
                'verbose_name_plural': 'TestQuestions',
            },
        ),
    ]