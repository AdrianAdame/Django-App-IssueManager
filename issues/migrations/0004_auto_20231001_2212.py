# Generated by Django 4.2.5 on 2023-10-02 05:12

from django.db import migrations

def populate_priority(apps, schemaeditor):
    entries = {
        "low": "An issue that can be completed with no to low deadline",
        "medium" : "An issue that can be completed within the deadline",
        "high" : "An issue that must be completed as soon as posible"
    }

    Priority = apps.get_model("issues", "Priority")

    for key, value in entries.items():
        role_obj = Priority(name = key, description = value)
        role_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0003_priority_issue_priority'),
    ]

    operations = [
        migrations.RunPython(populate_priority)
    ]
