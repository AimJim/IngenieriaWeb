# Generated by Django 4.1.2 on 2022-12-06 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appEmpresaCoche', '0012_marca_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='img_url',
            field=models.CharField(default='UwU', max_length=512),
            preserve_default=False,
        ),
    ]