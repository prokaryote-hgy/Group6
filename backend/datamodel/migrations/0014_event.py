# Generated by Django 3.2.5 on 2022-07-05 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamodel', '0013_auto_20210728_0636'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField()),
                ('eid', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('detail', models.CharField(max_length=200)),
            ],
        ),
    ]