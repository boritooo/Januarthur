# Generated by Django 5.0 on 2024-02-02 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sculpture',
            name='sculptor',
        ),
        migrations.RenameField(
            model_name='painting',
            old_name='painter',
            new_name='painters',
        ),
        migrations.AlterField(
            model_name='painter',
            name='group',
            field=models.ManyToManyField(related_name='painters', to='webapp.group'),
        ),
        migrations.DeleteModel(
            name='Sculptor',
        ),
        migrations.DeleteModel(
            name='Sculpture',
        ),
    ]
