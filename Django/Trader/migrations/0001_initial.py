# Generated by Django 4.2.3 on 2023-07-31 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cash', models.DecimalField(decimal_places=2, default=100000, max_digits=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trader.userprofile')),
            ],
        ),
    ]
