# Generated by Django 4.0.4 on 2022-05-08 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0005_alter_profilemodel_aadhar_card_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='Aadhar_Card',
            field=models.ImageField(upload_to='images/userprofile/adharcard'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='Pan_Card',
            field=models.ImageField(upload_to='images/userprofile/pancard'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='Salary_clip',
            field=models.FileField(blank=True, upload_to='images/userprofile/salarslips'),
        ),
    ]
