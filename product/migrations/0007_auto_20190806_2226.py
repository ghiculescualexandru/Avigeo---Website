# Generated by Django 2.2.4 on 2019-08-06 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20190806_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilajvanzare',
            name='firma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utilaje_vanzare', to='product.Firma'),
        ),
    ]