# Generated by Django 4.2.3 on 2023-12-07 00:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('category', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('file', models.FileField(upload_to='')),
                ('author', models.CharField(blank=True, max_length=256)),
                ('description', models.TextField(blank=True)),
                ('uploaderDescription', models.TextField(blank=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=64)),
                ('height', models.IntegerField(null=True)),
                ('width', models.IntegerField(null=True)),
                ('loop', models.BooleanField()),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mediaserver.gallery')),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mediaserver.media')),
            ],
        ),
        migrations.AddField(
            model_name='gallery',
            name='media_items',
            field=models.ManyToManyField(through='mediaserver.GalleryOrder', to='mediaserver.media'),
        ),
        migrations.AddConstraint(
            model_name='galleryorder',
            constraint=models.UniqueConstraint(fields=('media', 'gallery'), name='Every image has one gallery'),
        ),
    ]
