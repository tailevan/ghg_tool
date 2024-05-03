from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Inventory_Year(models.Model):
    year_choices = [(year, year) for year in range(2023, 2030)]
    year = models.IntegerField(choices=year_choices)

    def __str__(self):
        return str(self.year)

# scope 1
class Refrigerant(models.Model):
    inventory_year = models.ForeignKey(Inventory_Year, on_delete=models.CASCADE)
    TYPE_CHOICES = [
        ('R22', 'R22'),
        ('R410A', 'R410A'),
        ('HFC-134a', 'HFC-134a'),
        ('R600a', 'R600a'),
    ]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES) 
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    capacity = models.DecimalField(max_digits=10, decimal_places=2)
    emission = models.FloatField()

    
class Refrigerant_EF(models.Model):
    type = models.CharField(max_length=10)
    emission_factor = models.DecimalField(max_digits=10, decimal_places=5)


# scope 2
class Electricity(models.Model):
    inventory_year = models.ForeignKey(Inventory_Year, on_delete=models.CASCADE)
    consumption = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    emission = models.FloatField()

class Electricity_EF(models.Model):
    emission_factor = models.DecimalField(max_digits=10, decimal_places=5)

# scope 3 - commute
    
class Commute(models.Model):
    inventory_year = models.ForeignKey(Inventory_Year, on_delete=models.CASCADE)
    EMPLOYEE_CHOICES = [
        ('Nguyen Thuy Trang', 'Nguyen Thuy Trang'),
        ('Frank Pogade', 'Frank Pogade'),
        ('Than Xuan Mai', 'Than Xuan Mai'),
        ('Vu Thi Thom', 'Vu Thi Thom'),
        ('Chan', 'Chan'),
        ('Markus Klemmer', 'Markus Klemmer'),
        ('Nguyen Thi Thuy Trang', 'Nguyen Thi Thuy Trang'),
        ('Le Van Tai', 'Le Van Tai'),

    ]
    employee = models.CharField(max_length=30, choices=EMPLOYEE_CHOICES) 
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    workdays = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(365)])
    emission = models.FloatField()

# scope 3 - water
class Water(models.Model):
    inventory_year = models.ForeignKey(Inventory_Year, on_delete=models.CASCADE)
    consumption = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    emission = models.FloatField()
# scope 3 - waste

class Wastewater(models.Model):
    inventory_year = models.ForeignKey(Inventory_Year, on_delete=models.CASCADE)
    consumption = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    emission = models.FloatField()

# scope 3 - material
class Material(models.Model):
    inventory_year = models.ForeignKey(Inventory_Year, on_delete=models.CASCADE)
    MATERIAL_CHOICES = [
        ('Land line', 'Land line'),
        ('Tablet', 'Tablet'),
        ('Phone (Multifunction Device)', 'Phone (Multifunction Device)'),
        ('Camera Battery', 'Camera Battery'),
        ('Office Paper', 'Office Paper'),
        ('Toilet Paper', 'Toilet Paper'),
        ('Mixed Can', 'Mixed Can'),
        ('Office Chair', 'Office Chair'),
        ('Wooden Table', 'Wooden Table'),
        ('Bean Bag Chair', 'Bean Bag Chair'),
        ('Monitor - Desktop', 'Monitor - Desktop'),
        ('Office Desk', 'Office Desk'),
        ('Bottled Water (m3)', 'Bottled Water (m3)'),

    ]
    type = models.CharField(max_length=30, choices=MATERIAL_CHOICES) 
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    emission = models.FloatField()

class Material_EF(models.Model):
    type = models.CharField(max_length=30)
    emission_factor = models.DecimalField(max_digits=10, decimal_places=5)

# scope 3 - disposal
class Disposal(models.Model):
    inventory_year = models.ForeignKey(Inventory_Year, on_delete=models.CASCADE)
    DISPOSAL_CHOICES = [
        ('Carton Paper (Mixed Paper General)', 'Carton Paper (Mixed Paper General)'),
        ('Garbage (Mixed MSW)', 'Garbage (Mixed MSW)'),
        ('Plastic (Mixed Plastic)', 'Plastic (Mixed Plastic)'),

    ]
    type = models.CharField(max_length=40, choices=DISPOSAL_CHOICES) 
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    emission = models.FloatField()

class Disposal_EF(models.Model):
    type = models.CharField(max_length=40)
    emission_factor = models.DecimalField(max_digits=10, decimal_places=5)

# scope 3 - travel
class Travel(models.Model):
    inventory_year = models.ForeignKey(Inventory_Year, on_delete=models.CASCADE)
    TRAVEL_CHOICES = [
        ('Taxi - Grab Car', 'Taxi - Grab Car'),
        ('Motorbike (Grab)', 'Motorbike (Grab)'),
        ('Electric Taxi (Xanh Taxi)', 'Electric Taxi (Xanh Taxi)'),
    ]
    type = models.CharField(max_length=40, choices=TRAVEL_CHOICES)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    emission = models.FloatField()

class Travel_EF(models.Model):
    type = models.CharField(max_length=40)
    emission_factor = models.DecimalField(max_digits=10, decimal_places=10)

# scope 3 - flight
class Flight(models.Model):
    inventory_year = models.ForeignKey(Inventory_Year, on_delete=models.CASCADE)
    FLIGHT_CHOICES= [
        ('Domestic (Economy Class)', 'Domestic (Economy Class)'),
        ('International (Economy Class)', 'International (Economy Class)'),
    ]
    type = models.CharField(max_length=40, choices=FLIGHT_CHOICES)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    passenger = models.IntegerField(validators=[MinValueValidator(0)])
    date = models.DateField()
    emission = models.FloatField()

class Flight_EF(models.Model):
    type = models.CharField(max_length=40)
    emission_factor = models.DecimalField(max_digits=10, decimal_places=10)


# scope 3 - accommodation

class Accommodation(models.Model):
    inventory_year = models.ForeignKey(Inventory_Year, on_delete=models.CASCADE)
    ACCOMMODATION_CHOICES = [
        ('Vietnam', 'Vietnam'),
        ('Germany', 'Germany'),
        ('Hong Kong', 'Hong Kong'),
        ('Singapore', 'Singapore'),
        ('Thailand', 'Thailand'),
        ('Malaysia', 'Malaysia'),

    ]
    country = models.CharField(max_length=40, choices=ACCOMMODATION_CHOICES)
    night = models.IntegerField(validators=[MinValueValidator(0)])
    date = models.DateField()
    emission = models.FloatField()


class Freighting(models.Model):
    inventory_year = models.ForeignKey(Inventory_Year, on_delete=models.CASCADE)
    VEHICLE_CHOICES = [
        ('Electric Bike', 'Electric Bike'),
        ('Truck', 'Truck'),
        ('Train', 'Train'),
        ('Ship', 'Ship'),
        ('Airplane', 'Airplane'),
    ]
    AGENT_CHOICES = [
        ('Xanh SM', 'Xanh SM'),
        ('Grab', 'Grab'),
        ('Viettel Post', 'Viettel Post'),
        ('DHL', 'DHL'),
        ('UPS', 'UPS'),
        ('FedEx', 'FedEx'),
        ('Vietnam Post', 'Vietnam Post'),
    ]

    vehicle = models.CharField(max_length=40, choices=VEHICLE_CHOICES)
    agent = models.CharField(max_length=40, choices=AGENT_CHOICES)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    emission = models.FloatField()

class Freighting_EF(models.Model):
    vehicle = models.CharField(max_length=40)
    emission_factor = models.DecimalField(max_digits=10, decimal_places=10)