# Generated by Django 5.1.2 on 2024-12-02 15:35

import Tasks.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='attachments/', validators=[Tasks.validators.validate_file_size, Tasks.validators.validate_file_type])),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('communication_type', models.CharField(choices=[('email', 'Email'), ('chat', 'Chat'), ('video', 'Video Call'), ('voice', 'Voice Call')], max_length=20)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PeerReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[Tasks.validators.validate_min_length])),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('ongoing', 'Ongoing'), ('completed', 'Completed')], default='ongoing', max_length=20)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(blank=True, null=True, validators=[Tasks.validators.validate_due_date])),
                ('is_completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('efficiency_score', models.FloatField(blank=True, null=True)),
                ('resource_allocation', models.FloatField(blank=True, null=True)),
                ('complexity', models.FloatField(blank=True, null=True)),
                ('complexity_score', models.FloatField(blank=True, null=True)),
                ('estimated_duration', models.DurationField(blank=True, null=True)),
                ('ai_risk_assessment', models.FloatField(blank=True, null=True)),
                ('ai_success_prediction', models.FloatField(blank=True, null=True)),
                ('priority', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium', max_length=20)),
                ('budget', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('type', models.CharField(default='', max_length=100)),
                ('market_volatility', models.FloatField(blank=True, null=True)),
                ('economic_growth', models.FloatField(blank=True, null=True)),
                ('industry_disruption_level', models.FloatField(blank=True, null=True)),
                ('risk_level', models.CharField(default='medium', max_length=50)),
                ('collaboration_score', models.FloatField(blank=True, null=True)),
                ('team_structure', models.CharField(default='', max_length=100)),
                ('meeting_types', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_type', models.CharField(max_length=100)),
                ('allocated_amount', models.FloatField()),
                ('used_amount', models.FloatField(default=0)),
                ('ai_optimization_suggestion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('proficiency_level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, validators=[Tasks.validators.validate_min_length])),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, validators=[Tasks.validators.validate_min_length])),
                ('description', models.TextField(blank=True, validators=[Tasks.validators.validate_min_length])),
                ('priority', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium', max_length=10, validators=[Tasks.validators.validate_priority_level])),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('due_date', models.DateTimeField(blank=True, null=True, validators=[Tasks.validators.validate_due_date])),
                ('time_spent', models.DurationField(blank=True, null=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('recurring', models.BooleanField(default=False)),
                ('recurring_interval', models.CharField(blank=True, choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')], max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('progress', models.IntegerField(default=0, validators=[Tasks.validators.validate_task_progress])),
                ('status', models.CharField(default='pending', max_length=50)),
                ('all_day', models.BooleanField(default=False)),
                ('recurrence_rule', models.CharField(blank=True, max_length=200, null=True)),
                ('ai_complexity_score', models.FloatField(blank=True, null=True)),
                ('ai_estimated_duration', models.FloatField(blank=True, null=True)),
                ('complexity', models.FloatField(blank=True, null=True)),
                ('estimated_hours', models.FloatField(blank=True, null=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskDependency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dependency_type', models.CharField(choices=[('start_to_start', 'Start to Start'), ('start_to_finish', 'Start to Finish'), ('finish_to_start', 'Finish to Start'), ('finish_to_finish', 'Finish to Finish')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TaskSentiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentiment_score', models.FloatField()),
                ('sentiment_label', models.CharField(max_length=20)),
                ('analysis_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('ai_sentiment_analysis', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TimeLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProductivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('tasks_completed', models.IntegerField(default=0)),
                ('hours_worked', models.FloatField(default=0.0)),
                ('role', models.CharField(default='', max_length=100)),
                ('department', models.CharField(default='', max_length=100)),
                ('years_of_experience', models.IntegerField(default=0)),
                ('communication_preference', models.CharField(default='', max_length=50)),
                ('collaboration_score', models.FloatField(blank=True, null=True)),
                ('productivity_score', models.FloatField(default=0.0)),
                ('ai_productivity_insights', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('google_credentials', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[Tasks.validators.validate_min_length])),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('efficiency_score', models.FloatField(blank=True, null=True)),
                ('complexity_score', models.FloatField(blank=True, null=True)),
                ('estimated_duration', models.DurationField(blank=True, null=True)),
                ('automation_potential', models.FloatField(blank=True, null=True)),
                ('bottleneck_score', models.FloatField(blank=True, null=True)),
                ('optimization_score', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
