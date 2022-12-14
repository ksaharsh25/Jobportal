# Generated by Django 4.1.1 on 2022-10-07 09:32

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_aboutus_blog_contact_id_categories_aboutusimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='background',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='static/images/back')),
            ],
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='mid_description',
            field=tinymce.models.HTMLField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='overviewdescription',
            field=tinymce.models.HTMLField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog1descript',
            field=tinymce.models.HTMLField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog2descript',
            field=tinymce.models.HTMLField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog3descript',
            field=tinymce.models.HTMLField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog4descript',
            field=tinymce.models.HTMLField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog5descript',
            field=tinymce.models.HTMLField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog6descript',
            field=tinymce.models.HTMLField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='id',
            name='classes',
            field=models.CharField(blank=True, choices=[('1', '1'), ('4', '4'), ('2', '2'), ('5', '5'), ('3', '3')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='end_description',
            field=tinymce.models.HTMLField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='heading_description',
            field=tinymce.models.HTMLField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='mid_description',
            field=tinymce.models.HTMLField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='latestblog',
            name='blog1descript',
            field=tinymce.models.HTMLField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='latestblog',
            name='blog2descript',
            field=tinymce.models.HTMLField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='latestblog',
            name='blog3descript',
            field=tinymce.models.HTMLField(max_length=300, null=True),
        ),
    ]
