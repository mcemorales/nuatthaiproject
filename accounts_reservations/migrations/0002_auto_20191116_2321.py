# Generated by Django 2.2.7 on 2019-11-17 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account_reservation',
            name='massagetype',
            field=models.CharField(choices=[('N', 'NUAT THAI FOOT MASSAGE (1 HOUR) P350.00'), ('T', 'THAI BODY MASSAGE (1 HOUR) P350.00'), ('S', 'SWEDISH MASSAGE (1 HOUR) P400.00'), ('A', 'AROMATHERAPY MASSAGE (1 HOUR) P400.00'), ('E', 'EXPRESS - BACK AND HEAD (30 MINS) P250.00'), ('F', 'FOOT MASSAGE (30 HOUR) P250.00'), ('B', 'BACK MASSAGE (30 HOUR) P250.00'), ('H', 'HEAD MASSAGE (30 HOUR) P250.00')], max_length=100),
        ),
        migrations.AlterField(
            model_name='account_reservation',
            name='therapist',
            field=models.CharField(choices=[('F', 'FEMALE'), ('M', 'MALE')], max_length=50),
        ),
    ]
