from datetime import timedelta, date

from django.db import models
from django.utils import timezone

# Create your models here.
class Enquiry(models.Model):
    # Set default date to today + delta days
    def defaultDate(delta):
        return timezone.now() + timedelta(days=delta)

    name = models.CharField(
        max_length=50,
    )
    email = models.EmailField(
        max_length=80,
    )
    adults = models.SmallIntegerField(
        default=1,
    )
    children = models.SmallIntegerField(
        default=0,
    )
    enq_date_start = models.DateField(
        default=defaultDate(1),
    )
    enq_date_end = models.DateField(
        default=defaultDate(8),
    )
    sent_time = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return '%s, %s' % (self.name, self.email)
