# Generated by Django 2.1.3 on 2019-01-12 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_auto_20181121_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='asset_type',
            field=models.CharField(choices=[('server', '服务器'), ('networkdevice', '网络设备'), ('storagedevice', '存储设备'), ('securitydevice', '安全设备')], default='server', max_length=64, verbose_name='资产类型'),
        ),
    ]
