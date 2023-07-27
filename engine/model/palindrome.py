from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery


class Palindrome:
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.engine = SternmanEngine(
            last_service_date, current_mileage, last_service_mileage
        )
        self.battery = SpindlerBattery(last_service_date)

    def needs_service(self):
        engine_service_due = self.engine.needs_service()
        battery_service_due = self.battery.needs_service()

        return engine_service_due or battery_service_due
