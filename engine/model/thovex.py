from engine.capulet_engine import CapuletEngine
from battery.nubbin_battery import NubbinBattery


class Thovex:
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.engine = CapuletEngine(
            last_service_date, current_mileage, last_service_mileage
        )
        self.battery = NubbinBattery(last_service_date)

    def needs_service(self):
        engine_service_due = self.engine.needs_service()
        battery_service_due = self.battery.needs_service()

        return engine_service_due or battery_service_due
