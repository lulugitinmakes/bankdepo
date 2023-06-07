# Generated by Django 4.2.1 on 2023-06-06 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=222)),
                ('Dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=225)),
                ('districts', models.CharField(choices=[('kozhikode', 'malappuram'), ('eranakulam', 'kannur'), ('wayanad', 'palakkad')], default='kannur', max_length=15)),
                ('branches', models.CharField(choices=[('ramanatukara', 'omassery'), ('thamarassery', 'aluva'), ('vythiri', 'thalassery')], default='ramanatukara', max_length=15)),
                ('Acctype', models.CharField(max_length=200)),
                ('meterialprovide', models.CharField(choices=[('debitcard', 'creditcard')], default='debitcard', max_length=20)),
            ],
        ),
    ]