# Generated by Django 2.2.4 on 2019-08-05 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20190805_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilajdescription',
            name='utilaj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utilaj_descriptions', to='product.Utilaj'),
        ),
    ]
