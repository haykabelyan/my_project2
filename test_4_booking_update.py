import requests
import pytest
import allure
from my_data import MyData


@allure.feature('Booking Service')
@allure.suite('Update Booking Tests')
class TestBookingUpdate():
    data_for_put = [
        {
            "firstname": "Alice",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        },
        {
            "firstname": "Kim",
            "lastname": "Kardashian",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
    ]

    def setup_method(self):
        data = {"username": "admin", "password": "password123"}
        headers = {'Content-Type': 'application/json'}
        response = requests.post('https://restful-booker.herokuapp.com/auth', json=data, headers=headers)
        self.token = response.json().get('token')
        MyData.token = self.token

    @allure.title('Update Booking Information')
    @allure.description('This test verifies that booking information can be successfully updated.')
    @pytest.mark.parametrize('condition', data_for_put)
    @pytest.mark.regression
    def test_put_booking(self, condition):

        booking_id = MyData.booking_id

        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Cookie': f'token={self.token}'}
        response = requests.put(f'https://restful-booker.herokuapp.com/booking/{booking_id}', json=condition, headers=headers)

        with allure.step('Verify status code is 200'):
            assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

        response_data = response.json()
        if condition['firstname'] == 'Alice':
            with allure.step('Verify firstname'):
                assert condition['firstname'] == response_data['firstname'], f"Expected firstname {condition['firstname']}, but got {response_data['firstname']}"

            with allure.step('Verify lastname'):
                assert condition['lastname'] == response_data['lastname'], f"Expected lastname {condition['lastname']}, but got {response_data['lastname']}"

        if condition['firstname'] == 'Kim':
            with allure.step('Verify lastname for Kim'):
                assert condition['lastname'] == response_data['lastname'], f"Expected lastname {condition['lastname']} for Kim, but got {response_data['lastname']}"




    @allure.title('Attempt to Update Booking with Invalid Conditions')
    @allure.description('This test verifies that updating a booking with invalid token returns the appropriate error response.')
    @pytest.mark.parametrize('condition', data_for_put)
    @pytest.mark.regression
    def test_negative_put_booking(self, condition):

        booking_id = MyData.booking_id

        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Cookie': 'token=kim'}
        response = requests.put(f'https://restful-booker.herokuapp.com/booking/{booking_id}', json=condition, headers=headers)

        @allure.step('Verify status code is 403')
        def verify_status_code():
            assert response.status_code == 403, f'Expected Status Code 403, but got {response.status_code}'


