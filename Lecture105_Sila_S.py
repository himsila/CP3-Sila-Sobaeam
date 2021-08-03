class Vehicle:
    LicenseCode = ""
    SerialCode = ""
    Type = ""
    def TurnOnAirCond(self):
        print(f"({self.Type}) Turn On : AirCondition")

class Van(Vehicle):
    Type = "Van"

class PickUp(Vehicle):
    Type = "PickUp"

class SUV(Vehicle):
    Type = "SUV"

Van1 = Van()
PickUp1 = PickUp()
SUV1 = SUV()

Van1.TurnOnAirCond()
PickUp1.TurnOnAirCond()
SUV1.TurnOnAirCond()
