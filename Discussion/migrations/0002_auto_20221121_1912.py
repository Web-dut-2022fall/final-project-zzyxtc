# Generated by Django 2.1.5 on 2022-11-21 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Content', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Discussion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receive_notifies', to=settings.AUTH_USER_MODEL, verbose_name='接收者'),
        ),
        migrations.AddField(
            model_name='notification',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifies', to='Discussion.DiscussReply', verbose_name='回复'),
        ),
        migrations.AddField(
            model_name='notification',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_notifies', to=settings.AUTH_USER_MODEL, verbose_name='发送者'),
        ),
        migrations.AddField(
            model_name='discussreply',
            name='discuss',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replys', to='Discussion.Discuss'),
        ),
        migrations.AddField(
            model_name='discussreply',
            name='mentions',
            field=models.ManyToManyField(related_name='replys_from_reply', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='discussreply',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replys', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='discuss',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussions', to='Content.Book'),
        ),
        migrations.AddField(
            model_name='discuss',
            name='mentions',
            field=models.ManyToManyField(related_name='replys_from_discussion', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='discuss',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussions', to=settings.AUTH_USER_MODEL),
        ),
    ]
