# Generated by Django 4.2.6 on 2023-12-02 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_article_cover_alter_user_avatar_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
    ]
