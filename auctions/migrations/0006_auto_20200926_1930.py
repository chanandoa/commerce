# Generated by Django 3.0.8 on 2020-09-26 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_bid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='user',
            new_name='bidder',
        ),
    ]