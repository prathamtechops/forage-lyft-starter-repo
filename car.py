class Car:
    def __init__(self, engine, battery, tire_wear):
        self.engine = engine
        self.battery = battery
        self.tire_wear = tire_wear

    def needs_service(self):
        return (
            self.engine.needs_service()
            or self.battery.needs_service()
            or self._check_tire_service()
        )

    def _check_tire_service(self):
        if "Carrigan" in self.tire_wear:
            return any(wear >= 0.9 for wear in self.tire_wear["Carrigan"])
        elif "Octoprime" in self.tire_wear:
            return sum(self.tire_wear["Octoprime"]) >= 3
        else:
            return False
