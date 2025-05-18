import allure
import jsonschema
import pytest
import requests
from core.schemas.booking_schema import BOOKING_SCHEMA
from jsonschema import validate


@allure.title("Booking")
@allure.story("Create booking")
def test_create_booking(api_client):
    with allure.step("Generate payload"):
        booking_data = {
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
    with allure.step("Greate booking"):
        response = api_client.create_booking(booking_data)
    with allure.step("Booking validate"):
        jsonschema.validate(response, BOOKING_SCHEMA)