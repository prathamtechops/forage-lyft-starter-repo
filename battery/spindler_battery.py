import datetime


class SpindlerBattery:
    def __init__(self, last_service_date=None):
        self.last_service_date = last_service_date

    def set_last_service_date(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        if self.last_service_date is None:
            # If last_service_date is not set, consider the battery as due for service.
            return True

        current_date = datetime.date.today()
        years_since_last_service = (current_date - self.last_service_date).days / 365

        return years_since_last_service >= 2
