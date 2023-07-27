from datetime import datetime
from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery


class Calliope(CapuletEngine, SpindlerBattery):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        CapuletEngine.__init__(
            self, last_service_date, current_mileage, last_service_mileage
        )
        SpindlerBattery.__init__(self, last_service_date)

    def needs_service(self):
        engine_service_due = self.engine_should_be_serviced()
        battery_service_due = self.needs_battery_service()

        return engine_service_due or battery_service_due

    def needs_battery_service(self):
        return super().needs_service()
