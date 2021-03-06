# Generated by Django 2.2.6 on 2019-11-09 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0005_auto_20191109_1729'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='role',
            options={'verbose_name': 'Roles', 'verbose_name_plural': 'Roles'},
        ),
        migrations.CreateModel(
            name='AttdRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.Attd')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.Role')),
            ],
            options={
                'verbose_name': 'Attendance',
                'verbose_name_plural': 'Attendance',
                'unique_together': {('attd', 'role')},
            },
        ),
    ]
