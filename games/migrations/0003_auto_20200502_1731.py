# Generated by Django 2.2.7 on 2020-05-02 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20200502_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.GameCategory'),
        ),
        migrations.AlterField(
            model_name='playerscore',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Game'),
        ),
        migrations.AlterField(
            model_name='playerscore',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Player'),
        ),
    ]
