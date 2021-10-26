# Generated by Django 3.2.8 on 2021-10-26 09:41

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
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adv_name', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='image/%Y/%m/%d/')),
                ('video', models.FileField(blank=True, upload_to='video/%Y/%m/%d/')),
                ('file', models.FileField(blank=True, upload_to='file/%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['cat_name'],
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст отклика')),
                ('created_reply', models.DateTimeField(auto_now_add=True)),
                ('taken', models.BooleanField(default=False)),
                ('advert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='main_app.advert')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Отклик',
                'verbose_name_plural': 'Отклики',
                'ordering': ['-created_reply'],
            },
        ),
        migrations.CreateModel(
            name='Announcer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ann_name', models.CharField(max_length=250)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Объявитель',
                'verbose_name_plural': 'Объявители',
                'ordering': ['ann_name'],
            },
        ),
        migrations.AddField(
            model_name='advert',
            name='announcer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.announcer'),
        ),
        migrations.AddField(
            model_name='advert',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.category'),
        ),
    ]
