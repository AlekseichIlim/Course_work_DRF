# Generated by Django 4.2.2 on 2024-10-17 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="tg_chat_id",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Телеграмм chat-id"
            ),
        ),
    ]
