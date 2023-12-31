# Generated by Django 4.2.6 on 2023-10-26 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='project_images')),
                ('demo_link', models.URLField()),
                ('demo_video', models.FileField(blank=True, null=True, upload_to='project_videos')),
            ],
        ),
    ]
