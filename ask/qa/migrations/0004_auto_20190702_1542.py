# Generated by Django 2.2.2 on 2019-07-02 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0003_auto_20190702_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='addes_at',
            new_name='added_at',
        ),
    ]