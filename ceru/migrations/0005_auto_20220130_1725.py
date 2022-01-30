# Generated by Django 3.2 on 2022-01-30 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ceru', '0004_auto_20220130_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='booking',
            name='last_name',
            field=models.CharField(max_length=80),
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
    ]
