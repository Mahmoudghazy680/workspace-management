# Generated by Django 4.2.7 on 2023-11-04 22:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='check_in',
            field=models.DateTimeField(verbose_name='Check in '),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='check_out',
            field=models.DateField(blank=True, null=True, verbose_name='Check out '),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Customer Name '),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='total_1',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Total '),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='user_email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Customer E-mail '),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='user_phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Customer Phone '),
        ),
    ]
