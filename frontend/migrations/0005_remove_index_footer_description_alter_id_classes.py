# Generated by Django 4.1.1 on 2022-10-07 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_index_footer_description_index_footer_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='index',
            name='footer_description',
        ),
        migrations.AlterField(
            model_name='id',
            name='classes',
            field=models.CharField(blank=True, choices=[('4', '4'), ('3', '3'), ('5', '5'), ('1', '1'), ('2', '2')], max_length=1, null=True),
        ),
    ]
