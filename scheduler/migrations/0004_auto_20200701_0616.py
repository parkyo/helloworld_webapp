# Generated by Django 2.1 on 2020-07-01 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0003_auto_20200624_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Filters',
        ),
    ]
