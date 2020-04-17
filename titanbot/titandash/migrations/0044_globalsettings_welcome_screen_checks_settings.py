# Generated by Django 2.2.10 on 2020-04-17 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titandash', '0043_configuration_enable_forbidden_contract'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalsettings',
            name='welcome_screen_checks_settings',
            field=models.CharField(choices=[('on', 'On'), ('off', 'Off')], default='on', help_text='Enable or disable the option to check for the welcome screen while a bot is running (turning this off may improve performance if you have disabled the welcome screen in your settings).', max_length=255, verbose_name='Enable Welcome Screen Checks'),
        ),
    ]
