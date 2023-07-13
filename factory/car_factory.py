from datetime import date

from ..engine.capulet_engine import CapuletEngine
from ..engine.willoughby_engine import WilloughbyEngine
from ..engine.sternman_engine import SternmanEngine

from ..battery.spindler_battery import SpindlerBattery
from ..battery.nubbin_battery import NubbinBattery

from ..car import Car

class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, late_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(current_mileage = current_mileage, last_service_mileage = last_service_mileage)
        battery = SpindlerBattery(current_date = current_date, last_service_date = late_service_date)
        return Car(engine = engine, battery = battery)
    
    @staticmethod
    def create_glissade(current_date: date, late_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(current_mileage = current_mileage, last_service_mileage = last_service_mileage)
        battery = SpindlerBattery(current_date = current_date, last_service_date = late_service_date)
        return Car(engine = engine, battery = battery)
    
    @staticmethod
    def create_palindrome(current_date: date, late_service_date: date, warning_light_on: bool) -> Car:
        engine = SternmanEngine(warning_light_on = warning_light_on)
        battery = SpindlerBattery(current_date = current_date, last_service_date = late_service_date)
        return Car(engine = engine, battery = battery)
    
    @staticmethod
    def create_rorschach(current_date: date, late_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(current_mileage = current_mileage, last_service_mileage = last_service_mileage)
        battery = NubbinBattery(current_date = current_date, last_service_date = late_service_date)
        return Car(engine = engine, battery = battery)
    
    @staticmethod
    def create_thovex(current_date: date, late_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(current_mileage = current_mileage, last_service_mileage = last_service_mileage)
        battery = NubbinBattery(current_date = current_date, last_service_date = late_service_date)
        return Car(engine = engine, battery = battery)