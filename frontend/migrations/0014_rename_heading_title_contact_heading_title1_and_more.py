# Generated by Django 4.1.1 on 2022-10-07 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0013_rename_heading_title_blog_heading_title1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='heading_title',
            new_name='heading_title1',
        ),
        migrations.AddField(
            model_name='contact',
            name='heading_title2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='id',
            name='classes',
            field=models.CharField(blank=True, choices=[('3', '3'), ('1', '1'), ('5', '5'), ('4', '4'), ('2', '2')], max_length=1, null=True),
        ),
    ]
