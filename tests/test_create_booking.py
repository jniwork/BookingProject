import allure
import pytest
import requests


@allure.feature("Create booking")
@allure.story("Create booking with custom data")
def test_create_booking_with_custom_data(api_client):
    booking_data = {
        "firstname": "Nikolay",
        "lastname": "Zhuravlev",
        "totalprice": 250,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-04-20",
            "checkout": "2026-04-23"
        },
        "additionalneeds": "Dinner"
    }

    response = api_client.create_booking(booking_data)

    assert response["booking"]["firstname"] == booking_data["firstname"]
    assert response["booking"]["lastname"] == booking_data["lastname"]
    assert response["booking"]["totalprice"] == booking_data["totalprice"]
    assert response["booking"]["depositpaid"]
    assert response["booking"]["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"]
    assert response["booking"]["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"]
    assert response["booking"]["additionalneeds"] == booking_data["additionalneeds"]


def test_create_booking_with_random_data(api_client, generate_random_booking_data, booking_dates):
    booking_data = generate_random_booking_data
    booking_data["bookingdates"] = booking_dates

    response = api_client.create_booking(booking_data)

    assert response["booking"]["firstname"] == booking_data["firstname"]
    assert response["booking"]["lastname"] == booking_data["lastname"]
    assert response["booking"]["totalprice"] == booking_data["totalprice"]
    assert response["booking"]["depositpaid"]
    assert response["booking"]["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"]
    assert response["booking"]["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"]
    assert response["booking"]["additionalneeds"] == booking_data["additionalneeds"]

