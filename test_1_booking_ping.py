import allure
import pytest
import requests


@allure.feature('Ping Booking Service')
@allure.suite('Ping Tests')
class TestBookingGetPing():

    @allure.title('Check Booking Service Ping')
    @allure.description('This test verifies the ping endpoint of the booking service to ensure it is up and running.')
    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.severity('BLOCKER')
    def test_get_booking_ping(self):
        response = requests.get('https://restful-booker.herokuapp.com/ping')
        assert response.status_code == 201, f'Expected Status Code 201, but got {response.status_code}'


