# Generated by Django 2.1.4 on 2019-02-05 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0004_physicaladdress_postaladdress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generalenquiries',
            old_name='contactemail',
            new_name='contact_email',
        ),
        migrations.RenameField(
            model_name='generalenquiries',
            old_name='contactfax',
            new_name='contact_fax',
        ),
        migrations.RenameField(
            model_name='generalenquiries',
            old_name='contactperson',
            new_name='contact_person',
        ),
        migrations.RenameField(
            model_name='generalenquiries',
            old_name='contacttelephone',
            new_name='contact_telephone',
        ),
        migrations.RenameField(
            model_name='physicaladdress',
            old_name='physicaladdress',
            new_name='physical_address',
        ),
        migrations.RenameField(
            model_name='postaladdress',
            old_name='postaladdress',
            new_name='postal_address',
        ),
    ]