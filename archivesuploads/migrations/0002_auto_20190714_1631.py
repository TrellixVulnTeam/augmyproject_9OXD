# Generated by Django 2.2.2 on 2019-07-14 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archivesuploads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivesuploads',
            name='general_doi',
            field=models.TextField(max_length=20000),
        ),
        migrations.AlterField(
            model_name='archivesuploads',
            name='name',
            field=models.TextField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='archivesuploads',
            name='title',
            field=models.TextField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='archivesuploads',
            name='url',
            field=models.URLField(blank=True, max_length=5000, null=True),
        ),
    ]