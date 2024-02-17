from django.db import models

from apis.models import Service, SubService


class Appointment(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    customer_name = models.CharField(max_length=100)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    sub_service = models.ForeignKey(SubService, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'appointment'
        ordering = ['-id']

    def __str__(self):
        return f"{self.customer_name}'s appointment on {self.date} at {self.start_time}"

