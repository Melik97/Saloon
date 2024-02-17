from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=False)

    class Meta:
        db_table = 'service'
        ordering = ['-id']


class SubService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration_minutes = models.IntegerField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    class Meta:
        db_table = 'sub_service'
        ordering = ['-id']

    def __str__(self):
        return self.name

