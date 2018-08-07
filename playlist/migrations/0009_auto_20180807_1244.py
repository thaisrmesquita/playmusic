# Generated by Django 2.1 on 2018-08-07 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0008_auto_20180807_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('duration', models.TimeField()),
                ('year', models.DateField()),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playlist.Band', verbose_name='Band')),
            ],
            options={
                'verbose_name': 'Music',
                'verbose_name_plural': 'Musics',
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Playlist',
                'verbose_name_plural': 'Playlists',
            },
        ),
        migrations.AddField(
            model_name='music',
            name='playlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playlist.Playlist', verbose_name='Playlist'),
        ),
    ]
