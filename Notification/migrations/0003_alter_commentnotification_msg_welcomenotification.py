# Generated by Django 4.1 on 2022-11-07 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Notification', '0002_commentnotification_comment_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentnotification',
            name='msg',
            field=models.TextField(max_length=500),
        ),
        migrations.CreateModel(
            name='WelcomeNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('msg', models.TextField(max_length=500)),
                ('is_seen', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]