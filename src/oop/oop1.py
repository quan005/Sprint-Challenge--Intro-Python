# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle:
    # This is the bottom base of all classes
    def __init__(self):
        pass

class FlightVehicle(Vehicle):
    # Vehicle is the base of this class
    def __init__(self):
        pass

class Starship(FlightVehicle):
    # FlightVehicle is the base of this class
    def __init__(self):
        pass

class Airplane(FlightVehicle):
    # FlightVehicle is the base of this class
    def __init__(self):
        pass

class GroundVehicle(Vehicle):
    # Vehicle is the base of this class
    def __init__(self):
        pass

class Car(GroundVehicle):
    # GroundVehicle is the base of this class
    def __init__(self):
        pass

class Motorcycle(GroundVehicle):
    # GroundVehicle is the base of this class
    def __init__(self):
        pass