# Generated by Django 3.2.8 on 2021-11-16 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapApp', '0005_wwgveganclick_wwgzerowasteclick'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wwgclick',
            name='name',
        ),
        migrations.RemoveField(
            model_name='wwgveganclick',
            name='name',
        ),
        migrations.RemoveField(
            model_name='wwgzerowasteclick',
            name='name',
        ),
        migrations.AddField(
            model_name='wwgclick',
            name='index',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='wwgveganclick',
            name='index',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='wwgzerowasteclick',
            name='index',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='wwgclick',
            name='cnt',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='wwgveganclick',
            name='cnt',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='wwgzerowasteclick',
            name='cnt',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
