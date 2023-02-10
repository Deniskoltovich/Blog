# Generated by Django 4.1.5 on 2023-02-08 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=64)),
                ('content', models.CharField(max_length=1024)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('edited_time', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'draft'), ('published', 'published'), ('deleted', 'deleted')], default='draft', max_length=16)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.blog')),
            ],
            options={
                'ordering': ['-created_time'],
            },
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['blog'], name='posts_post_blog_id_dbe9f3_idx'),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['title'], name='posts_post_title_e7697c_idx'),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['content'], name='posts_post_content_3c9fae_idx'),
        ),
    ]
