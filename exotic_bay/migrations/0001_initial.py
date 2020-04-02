# Generated by Django 2.2.3 on 2020-04-02 21:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=100)),
                ('apartment_address', models.CharField(max_length=100)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('postcode', models.CharField(max_length=10)),
                ('address_type', models.CharField(choices=[('B', 'Billing'), ('S', 'Shipping')], max_length=1)),
                ('default', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('scientificName', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('type', models.CharField(choices=[('Reptiles', 'Reptiles'), ('Canidae', 'Canidae'), ('Amphibians', 'Amphibians'), ('Inverts', 'Inverts'), ('Marsupials', 'Marsupials')], max_length=10)),
                ('stock', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('careDetails', models.TextField()),
                ('orders', models.IntegerField(default=0)),
                ('date_added', models.DateField(default=datetime.date.today)),
                ('image', models.ImageField(blank=True, upload_to='pet_images')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pets', models.ManyToManyField(to='exotic_bay.Pet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_customer_id', models.CharField(blank=True, max_length=50, null=True)),
                ('one_click_purchasing', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PetOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exotic_bay.Pet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_charge_id', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('license', models.FileField(upload_to='licenses/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exotic_bay.Pet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(blank=True, max_length=20, null=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('being_delivered', models.BooleanField(default=False)),
                ('received', models.BooleanField(default=False)),
                ('billing_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_address', to='exotic_bay.Address')),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='exotic_bay.Payment')),
                ('pets', models.ManyToManyField(to='exotic_bay.PetOrder')),
                ('shipping_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_address', to='exotic_bay.Address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]