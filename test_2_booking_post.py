import allure
import requests
import pytest
from my_data import MyData


@allure.feature('Booking Service')
@allure.suite('Booking Creation Tests')
class TestBookingCreate:

    @allure.title('Create Booking and Verify Attributes')
    @allure.description('This test creates a new booking and verifies the attributes of the created booking.')
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_create_booking(self):
        data = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
        headers = {'Content-Type': 'application/json'}

        with allure.step('Send POST request to create a new booking'):
            response = requests.post(
                'https://restful-booker.herokuapp.com/booking',
                json=data,
                headers=headers
            )

        with allure.step('Verify the response status code is 200'):
            assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

        response_data = response.json()

        with allure.step('Verify the response contains "bookingid"'):
            assert 'bookingid' in response_data, "The response does not contain 'bookingid'"

        booking = response_data['booking']

        with allure.step('Verify firstname'):
            assert booking['firstname'] == data[
                'firstname'], f"Expected firstname {data['firstname']}, but got {booking['firstname']}"

        with allure.step('Verify lastname'):
            assert booking['lastname'] == data[
                'lastname'], f"Expected lastname {data['lastname']}, but got {booking['lastname']}"

        with allure.step('Verify totalprice'):
            assert booking['totalprice'] == data[
                'totalprice'], f"Expected totalprice {data['totalprice']}, but got {booking['totalprice']}"

        with allure.step('Verify depositpaid'):
            assert booking['depositpaid'] == data[
                'depositpaid'], f"Expected depositpaid {data['depositpaid']}, but got {booking['depositpaid']}"

        with allure.step('Verify checkin date'):
            assert booking['bookingdates']['checkin'] == data['bookingdates'][
                'checkin'], f"Expected checkin {data['bookingdates']['checkin']}, but got {booking['bookingdates']['checkin']}"

        with allure.step('Verify checkout date'):
            assert booking['bookingdates']['checkout'] == data['bookingdates'][
                'checkout'], f"Expected checkout {data['bookingdates']['checkout']}, but got {booking['bookingdates']['checkout']}"

        with allure.step('Verify additionalneeds'):
            assert booking['additionalneeds'] == data[
                'additionalneeds'], f"Expected additionalneeds {data['additionalneeds']}, but got {booking['additionalneeds']}"

        # Store the booking ID for future reference
        MyData.booking_id = response_data['bookingid']  # Assuming MyData is a class or object where you store this value
