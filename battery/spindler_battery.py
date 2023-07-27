from battery.battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        if self.last_service_date is None:
            return True

        years_since_last_service = (
            self.current_date - self.last_service_date
        ).days / 365

        return years_since_last_service >= 2
