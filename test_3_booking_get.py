import allure
import requests
from my_data import MyData
import pytest

@allure.feature('TEST BOOKING GET - feature')
@allure.suite('TEST BOOKING GET - suite')
class TestBookingGet():

    @allure.title('Test Retrieve All Bookings')
    @allure.description('This test case verifies that the system retrieves all bookings')
    @pytest.mark.regression
    def test_get_booking_all(self):
        with allure.step('Send GET request to the booking endpoint'):
            response = requests.get('https://restful-booker.herokuapp.com/booking')

        with allure.step('Verify the response status code is 200'):
            assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    @allure.title('Test Retrieve Booking By Id')
    @allure.description('This test case verifies that the system retrieves a specific booking by ID')
    @pytest.mark.regression
    def test_get_booking_by_id(self):
        booking_id = MyData.booking_id

        with allure.step(f'Send GET request to retrieve booking {booking_id}'):
            response = requests.get(f'https://restful-booker.herokuapp.com/booking/{booking_id}')

        with allure.step(f'Verify the response status code is 200 for booking {booking_id}'):
            assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

        response_data = response.json()

        with allure.step('Verify response data contains "firstname"'):
            assert 'firstname' in response_data, "The response does not contain 'firstname'"

        with allure.step('Verify response data contains "lastname"'):
            assert 'lastname' in response_data, "The response does not contain 'lastname'"

        with allure.step('Verify response data contains "bookingdates"'):
            assert 'bookingdates' in response_data, "The response does not contain 'bookingdates'"


