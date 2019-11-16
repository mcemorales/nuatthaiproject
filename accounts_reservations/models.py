from django.db import models
from django.contrib.auth.models import User


class account_reservation(models.Model):
    MASSAGE_TYPE = (
        ('N', 'NUAT THAI FOOT MASSAGE (1 HOUR) P350.00'),
        ('T', 'THAI BODY MASSAGE (1 HOUR) P350.00'),
        ('S', 'SWEDISH MASSAGE (1 HOUR) P400.00'),
        ('A', 'AROMATHERAPY MASSAGE (1 HOUR) P400.00'),
        ('E', 'EXPRESS - BACK AND HEAD (30 MINS) P250.00'),
        ('F', 'FOOT MASSAGE (30 HOUR) P250.00'),
        ('B', 'BACK MASSAGE (30 HOUR) P250.00'),
        ('H', 'HEAD MASSAGE (30 HOUR) P250.00'),
    )

    GENDER = (
        ('F', 'FEMALE'),
        ('M', 'MALE'),
    )

    reference_id = models.ForeignKey(User, on_delete=models.CASCADE)
    massagetype = models.CharField(max_length=100, choices=MASSAGE_TYPE)
    therapist = models.CharField(max_length=50, choices=GENDER)
    mobile_number = models.PositiveSmallIntegerField()
    date = models.DateField()
    time = models.TimeField()
    specialinstruction = models.TextField(blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reference_id
