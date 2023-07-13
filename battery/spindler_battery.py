from .battery import Battery
from dateutil.relativedelta import relativedelta

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        if ((self.current_date - self.last_service_date).days / 365.25) > 3:
            return True
        return False
