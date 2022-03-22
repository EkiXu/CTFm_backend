# Generated by Django 4.0.3 on 2022-03-22 04:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('challenge', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solutiondetail',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='challenge',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='challenges', to='challenge.challengecategory'),
        ),
    ]
