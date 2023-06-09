# Generated by Django 4.1.7 on 2023-03-07 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_post_recommended_post_top_pick_alter_post_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='primary_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='primary_category', to='posts.category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='categories', to='posts.category'),
        ),
    ]
