# Generated by Django 2.2.4 on 2019-08-26 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('describe', models.TextField(default='暂无描述内容')),
                ('constant', models.TextField(null=True)),
                ('findpage', models.TextField(null=True)),
                ('chapterpage', models.TextField(null=True)),
                ('contentpage', models.TextField(null=True)),
            ],
        ),
    ]