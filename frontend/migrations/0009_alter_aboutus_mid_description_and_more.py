# Generated by Django 4.1.1 on 2022-10-07 09:53

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0008_rename_about_us_index_about_us1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='mid_description',
            field=tinymce.models.HTMLField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='overviewdescription',
            field=tinymce.models.HTMLField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog1descript',
            field=tinymce.models.HTMLField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog2descript',
            field=tinymce.models.HTMLField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog3descript',
            field=tinymce.models.HTMLField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog4descript',
            field=tinymce.models.HTMLField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog5descript',
            field=tinymce.models.HTMLField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog6descript',
            field=tinymce.models.HTMLField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='id',
            name='classes',
            field=models.CharField(blank=True, choices=[('4', '4'), ('2', '2'), ('5', '5'), ('3', '3'), ('1', '1')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='aboutus_description',
            field=tinymce.models.HTMLField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='end_description',
            field=tinymce.models.HTMLField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='heading_description',
            field=tinymce.models.HTMLField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='mid_description',
            field=tinymce.models.HTMLField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='latestblog',
            name='blog1descript',
            field=tinymce.models.HTMLField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='latestblog',
            name='blog2descript',
            field=tinymce.models.HTMLField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='latestblog',
            name='blog3descript',
            field=tinymce.models.HTMLField(max_length=500, null=True),
        ),
    ]
