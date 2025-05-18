import allure
import pytest
import requests
from pydantic import ValidationError
from core.models.booking import BookingResponse
from faker import Faker


@allure.feature("Test create booking")
@allure.story("Positive: creating booking with custom data")
def test_create_booking_with_custom_data(api_client):
    booking_data = {
        "firstname": "Ivan",
        "lastname": "Ivanovich",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-02-01",
            "checkout": "2025-02-10"
        },
        "additionalneeds": "Dinner"
    }

    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f"Response validation failed: {e}")

    assert response["booking"]["firstname"] == booking_data["firstname"]
    assert response["booking"]["lastname"] == booking_data["lastname"]
    assert response["booking"]["totalprice"] == booking_data["totalprice"]
    assert response["booking"]["depositpaid"] == booking_data["depositpaid"]
    assert response["booking"]["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"]
    assert response["booking"]["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"]
    assert response["booking"]["additionalneeds"] == booking_data["additionalneeds"]


@allure.feature("Test create booking")
@allure.story("Positive: creating booking with random data")
def test_create_booking_with_random_data(api_client, generate_random_booking_data, booking_dates):
    booking_data = generate_random_booking_data
    booking_data["bookingdates"] = booking_dates

    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f"Response validation failed: {e}")

    assert response["booking"]["firstname"] == booking_data["firstname"]
    assert response["booking"]["lastname"] == booking_data["lastname"]
    assert response["booking"]["totalprice"] == booking_data["totalprice"]
    assert response["booking"]["depositpaid"] == booking_data["depositpaid"]
    assert response["booking"]["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"]
    assert response["booking"]["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"]
    assert response["booking"]["additionalneeds"] == booking_data["additionalneeds"]


@allure.feature("Test create booking")
@allure.story("Positive: creating booking without additionalneeds")
def test_create_booking_without_additionalneeds(api_client):
    booking_data = {
        "firstname": "Ivan",
        "lastname": "Ivanovich",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-02-01",
            "checkout": "2025-02-10"
        }
    }

    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f"Response validation failed: {e}")


@allure.feature("Test create booking")
@allure.story("Negative: creating booking with empty data")
def test_create_booking_with_empty_data(api_client):
    booking_data = {}

    with pytest.raises(requests.exceptions.HTTPError) as e:
        api_client.create_booking(booking_data)

    assert "500" in str(e.value), f"Expected 500 error but got {e.value}"


@allure.feature("Test create booking")
@allure.story("Negative: creating booking without firstname")
def test_create_booking_without_firstname(api_client, booking_dates):
    faker = Faker()
    booking_data = {
        "lastname": faker.last_name(),
        "totalprice": faker.random_number(digits=3),
        "depositpaid": faker.boolean(),
        "bookingdates": booking_dates
    }

    with pytest.raises(requests.exceptions.HTTPError) as e:
        api_client.create_booking(booking_data)

    assert "500" in str(e.value), f"Expected 500 error but got {e.value}"


@allure.feature("Test create booking")
@allure.story("Negative: creating booking without lastname")
def test_create_booking_without_firstname(api_client, booking_dates):
    faker = Faker()
    booking_data = {
        "firstname": faker.first_name(),
        "totalprice": faker.random_number(digits=3),
        "depositpaid": faker.boolean(),
        "bookingdates": booking_dates
    }

    with pytest.raises(requests.exceptions.HTTPError) as e:
        api_client.create_booking(booking_data)

    assert "500" in str(e.value), f"Expected 500 error but got {e.value}"


@allure.feature("Test create booking")
@allure.story("Negative: creating booking without totalprice")
def test_create_booking_without_firstname(api_client, booking_dates):
    faker = Faker()
    booking_data = {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "depositpaid": faker.boolean(),
        "bookingdates": booking_dates
    }

    with pytest.raises(requests.exceptions.HTTPError) as e:
        api_client.create_booking(booking_data)

    assert "500" in str(e.value), f"Expected 500 error but got {e.value}"


@allure.feature("Test create booking")
@allure.story("Negative: creating booking without depositpaid")
def test_create_booking_without_firstname(api_client, booking_dates):
    faker = Faker()
    booking_data = {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_number(digits=3),
        "bookingdates": booking_dates
    }

    with pytest.raises(requests.exceptions.HTTPError) as e:
        api_client.create_booking(booking_data)

    assert "500" in str(e.value), f"Expected 500 error but got {e.value}"


@allure.feature("Test create booking")
@allure.story("Negative: creating booking without bookingdates")
def test_create_booking_without_firstname(api_client, booking_dates):
    faker = Faker()
    booking_data = {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_number(digits=3),
        "depositpaid": faker.boolean()
    }

    with pytest.raises(requests.exceptions.HTTPError) as e:
        api_client.create_booking(booking_data)

    assert "500" in str(e.value), f"Expected 500 error but got {e.value}"
