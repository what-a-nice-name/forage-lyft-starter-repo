from battery.battery import Battery
from years import add_years


class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        battery_service_date = add_years(self.last_service_date, 4)
        if battery_service_date < self.current_date:
            return True
        else:
            return False
