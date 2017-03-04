# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-04 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('bid_main', '0004_user_roles_relation'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='may_manage_roles',
            field=models.ManyToManyField(
                blank=True,
                help_text='Users with this role will be able to grant or revoke those roles to any other user.',
                related_name='managers', to='bid_main.Role'),
        ),
    ]
