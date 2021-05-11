# Generated by Django 3.2.2 on 2021-05-06 17:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=255, unique=True)),
                ('unit_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('quantity', models.IntegerField(max_length=3)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('date_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer', verbose_name='Customer')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.products')),
            ],
        ),
    ]
