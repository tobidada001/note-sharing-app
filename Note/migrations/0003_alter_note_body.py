# Generated by Django 4.1 on 2024-04-12 05:44

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Note', '0002_alter_note_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
