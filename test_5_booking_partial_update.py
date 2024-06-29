import requests
import pytest
import allure
from my_data import MyData

@allure.feature('Booking Service Partial Update')
@allure.suite('Partial Update Booking Tests')
class TestBookingPartialUpdate():
    data_for_patch = [
        {
            "firstname": "Lilit",
            "lastname": "Brown"
        },
        {
            "firstname": "Loreta"
        }
    ]

    def setup_method(self):
        self.token = MyData.token

    @allure.title('Patch Booking with Various Conditions')
    @allure.description('This test verifies partial updates to booking information under various conditions.')
    @pytest.mark.parametrize('condition', data_for_patch)
    @pytest.mark.regression
    def test_patch_booking(self, condition):

        booking_id = MyData.booking_id

        response1 = requests.get(f'https://restful-booker.herokuapp.com/booking/{booking_id}')
        with allure.step('Verify status code is 200'):
            assert response1.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Cookie': f'token={self.token}'}
        response2 = requests.patch(f'https://restful-booker.herokuapp.com/booking/{booking_id}', json=condition, headers=headers)
        with allure.step('Verify status code is 200'):
            assert response1.status_code == 200, f'Expected Status Code 200, but got {response2.status_code}'

        response_data1 = response1.json()
        response_data2 = response2.json()

        if condition['firstname'] == 'Lilit':
            with allure.step('Verify firstname'):
                assert condition['firstname'] == response_data2['firstname'], f"Expected firstname {condition['firstname']}, but got {response_data2['firstname']}"

            with allure.step('Verify lastname'):
                assert condition['lastname'] == response_data2['lastname'], f"Expected lastname {condition['lastname']}, but got {response_data2['lastname']}"

            with allure.step('Verify additional needs'):
                assert response_data1['additionalneeds'] == response_data2['additionalneeds'],  f"Expected additional needs {response_data1['additionalneeds']}, but got {response_data2['additionalneeds']}"

        elif condition['firstname'] == 'Loreta':
            with allure.step('Verify firstname for Loreta'):
                assert condition['firstname'] == response_data2['firstname'], f"Expected firstname {condition['firstname']}, but got {response_data2['firstname']}"

            with allure.step('Verify additional needs for Loreta'):
                assert response_data1['additionalneeds'] == response_data2['additionalneeds'], f"Expected additional needs {response_data1['additionalneeds']}, but got {response_data2['additionalneeds']}"



    @allure.title('Negative Test Cases for Updating Booking')
    @allure.description('This test verifies that invalid update operations on bookings return appropriate error responses.')
    @pytest.mark.parametrize('condition', data_for_patch)
    @pytest.mark.regression
    def test_negative_put_booking(self, condition):

        booking_id = MyData.booking_id

        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Cookie': 'token=kim'}
        with allure.step('PATCH request'):
            response = requests.patch(f'https://restful-booker.herokuapp.com/booking/{booking_id}', json=condition, headers=headers)
        with allure.step('Make PATCH request and verify status code'):
            assert response.status_code == 403, f'Expected Status Code 403, but got {response.status_code}'

