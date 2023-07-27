import unittest
from datetime import date
from car_factory import CarFactory


class TestCarFactory(unittest.TestCase):
    def test_create_calliope(self):
        current_date = date(2023, 7, 26)
        last_service_date = date(2021, 7, 26)
        current_mileage = 50000
        last_service_mileage = 45000

        car = CarFactory.create_calliope(
            current_date, last_service_date, current_mileage, last_service_mileage
        )

        self.assertIsNotNone(car)
        self.assertEqual(car.engine.__class__.__name__, "CapuletEngine")
        self.assertEqual(car.battery.__class__.__name__, "SpindlerBattery")

    def test_create_glissade(self):
        current_date = date(2023, 7, 26)
        last_service_date = date(2022, 7, 26)
        current_mileage = 70000
        last_service_mileage = 65000

        car = CarFactory.create_glissade(
            current_date, last_service_date, current_mileage, last_service_mileage
        )

        self.assertIsNotNone(car)
        self.assertEqual(car.engine.__class__.__name__, "WilloughbyEngine")
        self.assertEqual(car.battery.__class__.__name__, "SpindlerBattery")

    def test_create_palindrome(self):
        current_date = date(2023, 7, 26)
        last_service_date = date(2020, 7, 26)
        warning_light_is_on = True

        car = CarFactory.create_palindrome(
            current_date, last_service_date, warning_light_is_on
        )

        self.assertIsNotNone(car)
        self.assertEqual(car.engine.__class__.__name__, "SternmanEngine")
        self.assertEqual(car.battery.__class__.__name__, "SpindlerBattery")

    def test_create_rorschach(self):
        current_date = date(2023, 7, 26)
        last_service_date = date(2020, 7, 26)
        current_mileage = 80000
        last_service_mileage = 75000

        car = CarFactory.create_rorschach(
            current_date, last_service_date, current_mileage, last_service_mileage
        )

        self.assertIsNotNone(car)
        self.assertEqual(car.engine.__class__.__name__, "WilloughbyEngine")
        self.assertEqual(car.battery.__class__.__name__, "NubbinBattery")

    def test_create_thovex(self):
        current_date = date(2023, 7, 26)
        last_service_date = date(2020, 7, 26)
        current_mileage = 55000
        last_service_mileage = 50000

        car = CarFactory.create_thovex(
            current_date, last_service_date, current_mileage, last_service_mileage
        )

        self.assertIsNotNone(car)
        self.assertEqual(car.engine.__class__.__name__, "CapuletEngine")
        self.assertEqual(car.battery.__class__.__name__, "NubbinBattery")


if __name__ == "__main__":
    unittest.main()
