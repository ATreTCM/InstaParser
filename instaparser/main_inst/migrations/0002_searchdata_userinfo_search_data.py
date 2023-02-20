# Generated by Django 4.1.5 on 2023-02-20 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_inst', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(max_length=100, verbose_name='ключевые слова')),
            ],
            options={
                'verbose_name': 'ключевое слово',
                'verbose_name_plural': 'ключевые слова',
                'ordering': ('keywords',),
            },
        ),
        migrations.AddField(
            model_name='userinfo',
            name='search_data',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main_inst.searchdata'),
            preserve_default=False,
        ),
    ]
