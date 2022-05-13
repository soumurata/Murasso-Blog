# Generated by Django 3.2.5 on 2022-05-13 14:20

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', mdeditor.fields.MDTextField()),
            ],
        ),
    ]
