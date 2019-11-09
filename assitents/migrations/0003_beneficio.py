# Generated by Django 2.0.5 on 2019-11-09 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assitents', '0002_evento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assitents.Evento')),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assitents.Participante')),
            ],
        ),
    ]
