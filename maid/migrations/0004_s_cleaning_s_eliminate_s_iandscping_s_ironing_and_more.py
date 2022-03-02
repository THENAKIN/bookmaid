# Generated by Django 4.0.1 on 2022-02-26 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maid', '0003_rename_service_ser_vice'),
    ]

    operations = [
        migrations.CreateModel(
            name='S_Cleaning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S_Cle_area', models.CharField(max_length=50)),
                ('S_Cle_area_price', models.IntegerField(max_length=10)),
                ('S_Cle_itme', models.IntegerField(max_length=10)),
                ('S_Cle_itme_price', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='S_Eliminate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S_Eli_itme', models.CharField(max_length=50)),
                ('S_Eli_itme_price', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='S_Iandscping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S_Ian_area', models.CharField(max_length=50)),
                ('S_Ian_area_price', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='S_Ironing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S_Iron_item', models.CharField(max_length=50)),
                ('S_Iron_itme_price', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='S_Massage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S_Mass_itme', models.IntegerField(max_length=10)),
                ('S_Mass_itme_price', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='S_Pool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S_Pool_item', models.CharField(max_length=50)),
                ('S_Pool_item_price', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=50)),
                ('s_img', models.ImageField(blank=True, upload_to='serpic')),
            ],
        ),
        migrations.DeleteModel(
            name='Ser_vice',
        ),
    ]