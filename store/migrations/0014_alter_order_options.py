# Generated by Django 4.2.6 on 2023-10-22 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_customer_options_remove_customer_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'permissions': [('cancel_order', 'Can Cancel Order')]},
        ),
    ]
