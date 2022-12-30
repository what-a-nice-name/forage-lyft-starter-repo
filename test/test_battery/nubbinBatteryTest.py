import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery


class NubbinBatteryTest(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2022-12-30")
        last_service_date = date.fromisoformat("2015-03-19")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2022-12-30")
        last_service_date = date.fromisoformat("2020-10-28")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

    
