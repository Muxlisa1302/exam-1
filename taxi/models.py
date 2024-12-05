from django.db import models

class TaxiRide(models.Model):
    name = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=20)
    driver_name = models.CharField(max_length=100)
    passenger_capacity = models.IntegerField()
    car_model = models.CharField(max_length=100)
    status = models.CharField(
        max_length=50,
        choices=[
            ('Available', 'Available'),
            ('Busy', 'Busy'),
            ('Under Maintenance', 'Under Maintenance'),
        ]
    )

    def __str__(self):
        return self.name
