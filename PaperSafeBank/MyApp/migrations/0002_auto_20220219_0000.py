# Generated by Django 3.1.10 on 2022-02-18 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='branch_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.branch'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notification',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
