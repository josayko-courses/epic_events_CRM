# Generated by Django 4.0.4 on 2022-05-15 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contracts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('attendees', models.IntegerField()),
                ('event_date', models.DateTimeField()),
                ('notes', models.CharField(max_length=256)),
                ('status', models.CharField(choices=[('NOT_OPEN', 'Not Open'), ('OPEN', 'Open'), ('CLOSE', 'Close')], max_length=32)),
                ('contract', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contracts.contract')),
                ('support_contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
