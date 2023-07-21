# Generated by Django 4.2.1 on 2023-07-21 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100)),
                ('name', models.CharField(max_length=120)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('description', models.TextField(max_length=2000)),
                ('quantity', models.IntegerField()),
                ('slug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.category')),
            ],
        ),
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('phone', models.IntegerField(max_length=12)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.product')),
            ],
        ),
    ]
