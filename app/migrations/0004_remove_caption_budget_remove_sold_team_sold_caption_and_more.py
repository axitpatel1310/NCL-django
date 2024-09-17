# Generated by Django 4.2.3 on 2024-09-14 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_caption_user_alter_caption_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caption',
            name='budget',
        ),
        migrations.RemoveField(
            model_name='sold',
            name='team',
        ),
        migrations.AddField(
            model_name='sold',
            name='caption',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.caption'),
        ),
        migrations.AlterField(
            model_name='sold',
            name='player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='app.player'),
        ),
        migrations.DeleteModel(
            name='Bid',
        ),
    ]
