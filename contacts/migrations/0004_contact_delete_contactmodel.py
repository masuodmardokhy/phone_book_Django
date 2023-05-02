# Generated by Django 4.2 on 2023-04-30 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contactmodel_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('family', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'مشخصات ',
                'verbose_name_plural': 'مشخصات کاربران',
            },
        ),
        migrations.DeleteModel(
            name='ContactModel',
        ),
    ]