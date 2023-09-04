# Generated by Django 4.1.7 on 2023-05-31 17:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aboutApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name=' 店铺名')),
                ('description', models.TextField(verbose_name='店铺详情描述')),
                ('publishDate', models.DateTimeField(default=django.utils.timezone.now, max_length=20, verbose_name='发布时间')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='浏览量')),
            ],
            options={
                'verbose_name': '店铺',
                'verbose_name_plural': '店铺',
                'ordering': ('-publishDate',),
            },
        ),
        migrations.CreateModel(
            name='StoreImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='Store/', verbose_name='店铺图片')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storeImgs', to='aboutApp.store', verbose_name='店铺')),
            ],
            options={
                'verbose_name': '店铺图片',
                'verbose_name_plural': '店铺图片',
            },
        ),
        migrations.DeleteModel(
            name='Award',
        ),
    ]
