# Generated by Django 2.1 on 2019-02-10 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_category_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='building',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
