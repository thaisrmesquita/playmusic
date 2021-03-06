# Generated by Django 2.1 on 2018-08-06 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0003_auto_20180806_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playlist.Genre', verbose_name='Genre')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playlist.Record', verbose_name='Record')),
            ],
            options={
                'verbose_name': 'Band',
                'verbose_name_plural': 'Bands',
            },
        ),
    ]
