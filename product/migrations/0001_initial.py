# Generated by Django 4.1 on 2022-08-12 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='상품명')),
                ('description', models.TextField(max_length=500, verbose_name='상품 설명')),
                ('price', models.IntegerField(verbose_name='가격')),
                ('start_date', models.DateTimeField(verbose_name='도입일')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성화 여부')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateTimeField(auto_now_add=True, verbose_name='구매일')),
                ('subscribe_start', models.DateTimeField(auto_now_add=True, verbose_name='구독 시작일')),
                ('subscribe_end', models.DateTimeField(verbose_name='구독 종료일')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'subscribes',
            },
        ),
    ]
