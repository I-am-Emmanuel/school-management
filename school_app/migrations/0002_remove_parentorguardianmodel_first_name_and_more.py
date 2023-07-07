# Generated by Django 4.1.3 on 2023-07-07 00:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parentorguardianmodel',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='parentorguardianmodel',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='staffmodel',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='staffmodel',
            name='last_name',
        ),
        migrations.AddField(
            model_name='parentorguardianmodel',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staffmodel',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='classroom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='school_app.classroom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='school_app.subject'),
            preserve_default=False,
        ),
    ]
