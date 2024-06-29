import requests
import pytest
import allure
from my_data import MyData


@allure.feature('Booking Service')
@allure.suite('Delete Booking Tests')
class TestBookingDelete():

    def setup_method(self):
        self.token = MyData.token

    @allure.title('Delete Non-Existent Booking')
    @allure.description('This test verifies that attempting to delete a booking that does not exist returns the appropriate error response.')
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_negative_delete_booking(self):
        booking_id = MyData.booking_id

        headers = {'Content-Type': 'application/json', 'Cookie': f'token=123345'}

        with allure.step('Make DELETE request'):
            response = requests.delete(f'https://restful-booker.herokuapp.com/booking/{booking_id}', headers=headers)

        with allure.step('Verify status code is 403'):
            assert response.status_code == 403, f'Expected Status Code 403, but got {response.status_code}'


    @allure.title('Delete Booking')
    @allure.description('This test verifies the deletion of a booking by its ID.')
    @pytest.mark.regression
    def test_delete_booking_by_id(self):
        booking_id = MyData.booking_id

        headers = {'Content-Type': 'application/json', 'Cookie': f'token={self.token}'}

        with allure.step('Delete booking'):
            response1 = requests.delete(f'https://restful-booker.herokuapp.com/booking/{booking_id}', headers=headers)

        with allure.step('Verify DELETE status code is 201'):
            assert response1.status_code == 201, f'Expected Status Code 201, but got {response1.status_code}'

        with allure.step('Verify booking is deleted'):
            response2 = requests.get(f'https://restful-booker.herokuapp.com/booking/{booking_id}')

        with allure.step('Verify GET status code is 404'):
            assert response2.status_code == 404, f'Expected Status Code 404, but got {response2.status_code}'

