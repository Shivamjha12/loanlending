# Generated by Django 4.0.4 on 2022-05-10 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanapp', '0007_loanrequestspost_accepted_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanrequestspost',
            name='accepted_user',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
