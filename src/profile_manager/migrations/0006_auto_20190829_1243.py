# Generated by Django 2.0.13 on 2019-08-29 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_manager', '0005_profile_get_messages_by_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='preferred_internal_only',
            field=models.BooleanField(default=False, help_text='Check this if you want your preferred name used ONLY in the classroom, but NOT in other places such as on your report card.', verbose_name='Use preferred first name internally only'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='preferred_name',
            field=models.CharField(blank=True, help_text='If you would prefer your teacher to call you by a name other than                                       the name on your school records, please put it here.', max_length=50, null=True, verbose_name='Preferred first name'),
        ),
    ]
