# Generated by Django 4.0.3 on 2022-04-06 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_likes_image_likes_count_remove_image_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.profile'),
            preserve_default=False,
        ),
    ]