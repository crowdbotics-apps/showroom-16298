# Generated by Django 2.2.12 on 2020-04-27 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task_profile', '0001_initial'),
        ('task_category', '0001_initial'),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('status', models.CharField(max_length=10)),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('tip', models.FloatField(blank=True, null=True)),
                ('timestamp_arrived', models.DateTimeField(blank=True, null=True)),
                ('timestamp_completed', models.DateTimeField(blank=True, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasktransaction_customer', to='task_profile.CustomerProfile')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasktransaction_location', to='location.MapLocation')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasktransaction_subcategory', to='task_category.Subcategory')),
                ('tasker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasktransaction_tasker', to='task_profile.TaskerProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rating_customer', to='task_profile.CustomerProfile')),
                ('tasker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_tasker', to='task_profile.TaskerProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_customer', to='task_profile.CustomerProfile')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='message_task', to='task.TaskTransaction')),
                ('tasker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_tasker', to='task_profile.TaskerProfile')),
            ],
        ),
    ]
