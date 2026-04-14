from django.db import migrations, models

class Migrations(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name= 'Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname' = models.Charfield(max_length=255)),
                ('lastname' = models.Charfield(max_length=255)),
            ],
        ),
    ],