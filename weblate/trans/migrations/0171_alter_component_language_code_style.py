# Generated by Django 4.2.2 on 2023-06-10 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0170_component_screenshot_filemask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='language_code_style',
            field=models.CharField(blank=True, choices=[('', 'Default based on the file format'), ('posix', 'POSIX style using underscore as a separator'), ('bcp', 'BCP style using hyphen as a separator'), ('posix_long', 'POSIX style using underscore as a separator, including country code'), ('posix_long_lowercase', 'POSIX style using underscore as a separator, including country code (lowercase)'), ('bcp_long', 'BCP style using hyphen as a separator, including country code'), ('bcp_legacy', 'BCP style using hyphen as a separator, legacy language codes'), ('bcp_lower', 'BCP style using hyphen as a separator, lower cased'), ('android', 'Android style'), ('appstore', 'Apple App Store metadata style'), ('googleplay', 'Google Play metadata style'), ('linux', 'Linux style')], default='', help_text='Customize language code used to generate the filename for translations created by Weblate.', max_length=20, verbose_name='Language code style'),
        ),
    ]
