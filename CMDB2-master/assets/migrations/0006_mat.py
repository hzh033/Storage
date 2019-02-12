# Generated by Django 2.1.3 on 2019-01-31 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_auto_20190112_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mat_id', models.IntegerField(max_length=64, unique=True, verbose_name='序列')),
                ('mat_name', models.CharField(max_length=64, unique=True, verbose_name='资产名称')),
                ('major', models.CharField(choices=[(0, '无线'), (1, '传输'), (2, '家宽'), (3, '土建'), (4, '电力')], max_length=64, verbose_name='专业类别')),
                ('version', models.CharField(max_length=64, verbose_name='型号')),
                ('materiel_amount', models.IntegerField(max_length=64, verbose_name='数量')),
                ('company', models.CharField(choices=[(0, '中兴'), (1, '京信'), (2, '三维'), (3, '华为'), (4, '烽火'), (5, '其他')], max_length=64, verbose_name='生产厂家')),
                ('materiel_num', models.CharField(max_length=64, verbose_name='货单编号')),
                ('remark1', models.CharField(max_length=64, verbose_name='材料备注1')),
                ('remark2', models.CharField(max_length=64, verbose_name='材料备注2')),
                ('source', models.CharField(max_length=64, verbose_name='来源')),
            ],
        ),
    ]
