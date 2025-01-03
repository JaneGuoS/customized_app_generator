# Generated by Django 5.1.4 on 2024-12-24 23:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('body', models.TextField(verbose_name='body')),
                ('published', models.BooleanField(default=False, verbose_name='published')),
                ('published_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
            },
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_id', models.IntegerField(verbose_name='businessId')),
                ('relation_type', models.CharField(max_length=255, verbose_name='relationType')),
                ('parent_id', models.IntegerField(unique=True, verbose_name='parentId')),
                ('entity_id', models.IntegerField(verbose_name='entityId')),
            ],
            options={
                'verbose_name': 'relation',
                'verbose_name_plural': 'relations',
            },
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveSmallIntegerField()),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.count')),
            ],
        ),
        migrations.CreateModel(
            name='EventGuide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.event')),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.event')),
            ],
            options={
                'verbose_name': 'awesome guest',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.event', verbose_name='awesome event')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='body')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post', verbose_name='post')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('status', models.CharField(max_length=255, verbose_name='status')),
                ('created_date', models.DateField(blank=True, null=True)),
                ('count', models.IntegerField(verbose_name='count')),
                ('channel_relations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channelRelations', related_query_name='channelRelations', to='blog.relation', to_field='parent_id')),
            ],
            options={
                'verbose_name': 'channel',
                'verbose_name_plural': 'channels',
            },
        ),
    ]
