# Generated by Django 2.0 on 2017-12-21 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Combat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Fecha/hora')),
            ],
        ),
        migrations.AlterModelOptions(
            name='fighter',
            options={'verbose_name': 'Luchador', 'verbose_name_plural': 'Luchadores'},
        ),
        migrations.AlterModelOptions(
            name='tournament',
            options={'verbose_name': 'Torneo', 'verbose_name_plural': 'Torneos'},
        ),
        migrations.AddField(
            model_name='combat',
            name='fighter1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='figher1', to='main.Fighter', verbose_name='Luchador 1'),
        ),
        migrations.AddField(
            model_name='combat',
            name='fighter2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fither2', to='main.Fighter', verbose_name='Luchador 2'),
        ),
        migrations.AddField(
            model_name='combat',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Tournament', verbose_name='Torneo'),
        ),
    ]
