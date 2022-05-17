# Generated by Django 4.0.4 on 2022-05-17 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('main', '0003_basepage_articlepage_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover_photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
