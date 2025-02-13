# Generated by Django 5.1.2 on 2024-12-02 15:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AI', '0001_initial'),
        ('Tasks', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='aifeedback',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='aiprediction',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AI.aimodel'),
        ),
        migrations.AddField(
            model_name='aiprediction',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tasks.task'),
        ),
        migrations.AddField(
            model_name='aiprediction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='aifeedback',
            name='prediction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AI.aiprediction'),
        ),
        migrations.AddField(
            model_name='airecommendation',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AI.aimodel'),
        ),
        migrations.AddField(
            model_name='airecommendation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='aifeedback',
            name='recommendation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AI.airecommendation'),
        ),
        migrations.AddField(
            model_name='communication',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Tasks.project'),
        ),
        migrations.AddField(
            model_name='communication',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ai_received_communications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='communication',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ai_sent_communications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='communication',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Tasks.task'),
        ),
        migrations.AddField(
            model_name='peerreview',
            name='reviewee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ai_reviews_received', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='peerreview',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ai_reviews_given', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='peerreview',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tasks.task'),
        ),
    ]
