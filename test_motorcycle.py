import pytest
from motorcycle_shop import calculate_monthly_payment, calculate_total_payment

def test_calculate_monthly_payment():
    # Test case 1: Minimum down payment, no interest
    car_price = 100000
    down_payment = 20000
    monthly_payment = calculate_monthly_payment(car_price, down_payment)
    assert monthly_payment == 6666.67

    # Test case 2: Minimum down payment, with interest
    car_price = 80000
    down_payment = 16000
    interest_rate = 0.05
    monthly_payment = calculate_monthly_payment(car_price, down_payment, interest_rate)
    assert monthly_payment == 5786.67

    # Test case 3: Down payment less than 20%
    car_price = 90000
    down_payment = 15000
    with pytest.raises(ValueError):
        monthly_payment = calculate_monthly_payment(car_price, down_payment)

def test_calculate_total_payment():
    # Test case 1: Minimum down payment, no interest
    car_price = 100000
    down_payment = 20000
    total_payment = calculate_total_payment(car_price, down_payment)
    assert total_payment == 100000

    # Test case 2: Minimum down payment, with interest
    car_price = 80000
    down_payment = 16000
    interest_rate = 0.05
    total_payment = calculate_total_payment(car_price, down_payment, interest_rate)
    assert total_payment == 84000

    # Test case 3: Down payment less than 20%
    car_price = 90000
    down_payment = 15000
    with pytest.raises(ValueError):
        total_payment = calculate_total_payment(car_price, down_payment)


# import unittest
# from main import calculate_monthly_payment

# class TestMotorcycleShop(unittest.TestCase):
    
#     def test_calculate_monthly_payment(self):
#         # Test case 1: Minimum down payment
#         price = 10000
#         down_payment = 2000
#         monthly_payment = calculate_monthly_payment(price, down_payment)
#         expected_payment = 666.67
#         self.assertAlmostEqual(monthly_payment, expected_payment, places=2)
        
#         # Test case 2: Higher down payment
#         price = 15000
#         down_payment = 4000
#         monthly_payment = calculate_monthly_payment(price, down_payment)
#         expected_payment = 916.67
#         self.assertAlmostEqual(monthly_payment, expected_payment, places=2)
        
#         # Test case 3: Lowest possible price
#         price = 1000
#         down_payment = 200
#         monthly_payment = calculate_monthly_payment(price, down_payment)
#         expected_payment = 66.67
#         self.assertAlmostEqual(monthly_payment, expected_payment, places=2)
        
#         # Test case 4: Lowest possible down payment
#         price = 5000
#         down_payment = 1000
#         monthly_payment = calculate_monthly_payment(price, down_payment)
#         expected_payment = 375.00
#         self.assertAlmostEqual(monthly_payment, expected_payment, places=2)