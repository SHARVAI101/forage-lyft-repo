import unittest
from datetime import date

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

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
        current_date = date.fromisoformat("2023-07-13")
        last_service_date = date.fromisoformat("2019-01-25")
        battery = SpindlerBattery(current_date=current_date, last_service_date=last_service_date)
        self.assertTrue(battery.needs_service())
    
    def test_spindler_should_not_be_serviced(self):
        current_date = date.fromisoformat("2023-07-13")
        last_service_date = date.fromisoformat("2022-01-25")
        battery = SpindlerBattery(current_date=current_date, last_service_date=last_service_date)
        self.assertFalse(battery.needs_service())
    
    def test_nubbin_should_be_serviced(self):
        current_date = date.fromisoformat("2023-07-13")
        last_service_date = date.fromisoformat("2018-01-25")
        battery = NubbinBattery(current_date=current_date, last_service_date=last_service_date)
        self.assertTrue(battery.needs_service())
    
    def test_nubbin_should_not_be_serviced(self):
        current_date = date.fromisoformat("2023-07-13")
        last_service_date = date.fromisoformat("2022-01-25")
        battery = NubbinBattery(current_date=current_date, last_service_date=last_service_date)
        self.assertFalse(battery.needs_service())

class TestTires(unittest.TestCase):
    def test_carrigan_should_be_serviced(self):
        tires = CarriganTires(wear=[0.2, 0.3, 0.4, 0.95])
        self.assertTrue(tires.needs_service())

    def test_carrigan_should_not_be_serviced(self):
        tires = CarriganTires(wear=[0.2, 0.3, 0.4, 0.5])
        self.assertFalse(tires.needs_service())
    
    def test_octoprime_should_be_serviced(self):
        tires = OctoprimeTires(wear=[0.8, 0.9, 0.8, 0.95])
        self.assertTrue(tires.needs_service())

    def test_octoprime_should_not_be_serviced(self):
        tires = OctoprimeTires(wear=[0.2, 0.3, 0.4, 0.5])
        self.assertFalse(tires.needs_service())
    
if __name__ == '__main__':
    unittest.main()
