# Generated by Django 4.1.1 on 2022-10-07 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0012_remove_aboutus_overviewdescription_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='heading_title',
            new_name='heading_title1',
        ),
        migrations.AddField(
            model_name='blog',
            name='heading_title2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='mid_description',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='id',
            name='classes',
            field=models.CharField(blank=True, choices=[('3', '3'), ('4', '4'), ('5', '5'), ('2', '2'), ('1', '1')], max_length=1, null=True),
        ),
    ]