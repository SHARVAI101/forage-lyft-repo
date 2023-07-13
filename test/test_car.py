import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

class TestEngine(unittest.TestCase):
    def test_capulet_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_capulet_should_not_be_serviced(self):
        current_mileage = 10000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_willoughby_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_willoughby_should_not_be_serviced(self):
        current_mileage = 10000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_sternman_should_be_serviced(self):
        engine = SternmanEngine(warning_light_on=True)
        self.assertTrue(engine.needs_service())

    def test_sternman_should_not_be_serviced(self):
        engine = SternmanEngine(warning_light_on=False)
        self.assertFalse(engine.needs_service())

class TestBattery(unittest.TestCase):
    def test_spindler_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = SpindlerBattery(current_date=today, last_service_date=last_service_date)
        self.assertTrue(battery.needs_service())
    
    def test_spindler_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = SpindlerBattery(current_date=today, last_service_date=last_service_date)
        self.assertFalse(battery.needs_service())
    
    def test_nubbin_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(current_date=today, last_service_date=last_service_date)
        self.assertTrue(battery.needs_service())
    
    def test_nubbin_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = NubbinBattery(current_date=today, last_service_date=last_service_date)
        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
