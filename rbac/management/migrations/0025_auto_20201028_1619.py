# Generated by Django 2.2.4 on 2020-10-28 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("management", "0024_access_permission")]

    operations = [
        migrations.AddField(model_name="access", name="permission", field=models.TextField(default="*:*:*")),
        migrations.AlterField(model_name="access", name="perm", field=models.TextField(null=True)),
    ]
