# Generated by Django 3.2.8 on 2021-11-12 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapApp', '0003_vegan'),
    ]

    operations = [
        migrations.CreateModel(
            name='WwgClick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('cnt', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WwgVegan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('number', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('imgURL', models.CharField(max_length=1000)),
                ('img', models.CharField(max_length=300)),
                ('lat', models.IntegerField()),
                ('lng', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WwgZerowaste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('number', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('imgURL', models.CharField(max_length=1000)),
                ('img', models.CharField(max_length=300)),
                ('lat', models.IntegerField()),
                ('lng', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='vegan',
        ),
        migrations.DeleteModel(
            name='wwg_place',
        ),
        migrations.DeleteModel(
            name='zerowaste',
        ),
        migrations.RenameField(
            model_name='wwguser',
            old_name='user_name',
            new_name='user_birthyear',
        ),
    ]
