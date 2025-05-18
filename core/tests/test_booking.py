import allure
import jsonschema
import pytest
import requests
from core.schemas.booking_schema import BOOKING_SCHEMA
from jsonschema import validate


@allure.title("Booking")
@allure.story("Create booking")
def test_create_booking(api_client, generate_random_booking_data, booking_dates):
    with allure.step("Generate payload"):
        booking_data = generate_random_booking_data
        booking_data["bookingdates"] = booking_dates
    with allure.step("Create booking"):
        response = api_client.create_booking(booking_data)
    with allure.step("Booking validate"):
        jsonschema.validate(response, BOOKING_SCHEMA)
