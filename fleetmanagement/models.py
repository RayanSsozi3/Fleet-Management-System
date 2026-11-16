from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


def validate_text_only(value):
    if not all(char.isalpha() for char in value):
        raise ValidationError("Only letters are allowed.")

    
class Car(models.Model):
    TRANSIT_OPTIONS = [
        ("A", "Auto"),
        ("M", "Manual")
    ]
    ENGINE_OPTIONS = [
        ("P", "Petrol"),
        ("D", "Diesel")
    ]
    car_type = models.CharField(max_length=10, verbose_name="Car Type")
    Brand = models.CharField(max_length=10, verbose_name="Brand Name", validators=[validate_text_only])
    number_plate = models.CharField(max_length=7, unique=True, verbose_name="Number Plate")
    Model = models.CharField(max_length=20)
    Expiry_insurance = models.DateField(auto_now=False)
    Transmission = models.CharField(max_length=10, choices=TRANSIT_OPTIONS)
    Engine_type = models.CharField(max_length=10, choices=ENGINE_OPTIONS, verbose_name="Engine Type")

    def __str__(self):
            return self.number_plate

class Staff(models.Model):
    GENDER_OPTIONS = [
       ("M", "Male"),
       ("F", "Female")
    ]
    ROLE_OPTIONS = [
        ("D", "Driver"),
        ("M", "Manager")
    ]
    first_name = models.CharField(max_length=50, verbose_name="First Name", validators=[validate_text_only])
    second_name = models.CharField(max_length=20, verbose_name="Second Name", validators=[validate_text_only])
    gender = models.CharField(max_length=2, choices=GENDER_OPTIONS)
    role = models.CharField(max_length=2, choices=ROLE_OPTIONS)
    contact = models.CharField(max_length=10, verbose_name="Contact Number", unique=True)

    def __str__(self):
        return str(self.id)

class Assigning(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete = models.CASCADE)
    number_plate = models.ForeignKey(Car, on_delete= models.CASCADE)
    assignment_date = models.DateField(auto_now=False, verbose_name="Assignment Date")

class Fuelling(models.Model):
    STATION_OPTIONS = [
        ("S", "Shell"),
        ("T", "Total")
    ]
    vehicle_id = models.ForeignKey(Car, on_delete = models.CASCADE)
    station = models.CharField(max_length=20, choices=STATION_OPTIONS)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    price = models.PositiveIntegerField(validators=[MinValueValidator(5000)])
    date = models.DateField(auto_now=False)

    @property
    def total_cost(self):
        # Calculated field: total_cost = quantity * price
        return self.quantity * self.price

class Repair_issues(models.Model):
    problem = models.CharField(max_length=20,)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    measure = models.PositiveIntegerField()
    unit_cost = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return str(self.id)

class Repair_records(models.Model):
    PROVIDER_OPTIONS = [
        ("AC", "AutoCare"),
        ("AF", "AutoFix")
    ]
    repair_id = models.ForeignKey(Repair_issues, on_delete = models.CASCADE)
    Vehicle_id = models.ForeignKey(Car, on_delete = models.CASCADE)
    repair_center = models.CharField(max_length=20, choices=PROVIDER_OPTIONS, verbose_name="Repair Center")
    repair_date = models.DateField(auto_now=False, verbose_name="Repair Date")

    @property
    def cost(self):
        # Calculated field: cost = quantity * unit_cost (from the linked Repair_issues)
        return self.repair_id.quantity * self.repair_id.unit_cost

class Service_issues(models.Model):
    service_item = models.CharField(max_length=20, verbose_name="Service Item")
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    measure = models.PositiveIntegerField()
    unit_cost = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
            return str(self.id)
    
class Service_records(models.Model):
    PROVIDER_OPTIONS = [
        ("AC", "AutoCare"),
        ("AF", "AutoFix")
    ]
    Service_id = models.ForeignKey(Service_issues, on_delete = models.CASCADE)
    Vehicle_id = models.ForeignKey(Car, on_delete = models.CASCADE)
    service_center = models.CharField(max_length=20, choices=PROVIDER_OPTIONS)
    service_date = models.DateField(auto_now=False, verbose_name="Service Date")

    @property
    def cost(self):
        # Calculated field: cost = quantity * unit_cost (from the linked Service_issues)
        return self.Service_id.quantity * self.Service_id.unit_cost
    