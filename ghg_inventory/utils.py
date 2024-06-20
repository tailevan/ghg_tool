from decimal import Decimal


def calculate_emission_refrigerant(quantity, capcity, refrigerant_ef):
    emission = Decimal(quantity) * Decimal(capcity) * (Decimal(0.06) + Decimal(0.16) * Decimal(refrigerant_ef)*Decimal(1e-3))
    return emission

def calculate_emission_electricity(consumption, electricity_ef):
    emission = Decimal(consumption) * Decimal(electricity_ef)
    return emission


def calculate_emission_commute(distance, workdays):
    emission = Decimal(distance) * Decimal(workdays) * Decimal(0.00048848)
    return emission

def calculate_emission_water(consumption):
    emission = Decimal(consumption) * Decimal(0.000259956)
    return emission

def calculate_emission_wastewater(consumption):
    emission = Decimal(consumption) * Decimal(0.000272)
    return emission

def calculate_emission_material(consumption, material_ef):
    emission = Decimal(consumption) * Decimal(0.001) * Decimal(material_ef)
    return emission

def calculate_emission_disposal(amount, disposal_ef):
    emission = Decimal(amount) * Decimal(disposal_ef) * Decimal(0.001)
    return emission

def calculate_emission_travel(distance, travel_ef):
    emission = Decimal(distance) * Decimal(travel_ef)
    return emission

def calculate_emission_flight(distance, passenger, flight_ef):
    emission = Decimal(distance) * Decimal(flight_ef) / Decimal(passenger)
    return emission

def calculate_emission_accommodation(night):
    emission = Decimal(night) * Decimal(0.0385)
    return emission

def calculate_emission_freighting(distance, freighting_ef):
    emission = Decimal(distance) * Decimal(freighting_ef)
    return emission


