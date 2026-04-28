import allure
import pytest
import requests
from pydantic import ValidationError
from core.models.booking import BookingResponse


@allure.feature("Create booking")
@allure.story("Positive: Create booking with custom data")
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
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f"Response validation error: {e}")

    assert response["booking"]["firstname"] == booking_data["firstname"]
    assert response["booking"]["lastname"] == booking_data["lastname"]
    assert response["booking"]["totalprice"] == booking_data["totalprice"]
    assert response["booking"]["depositpaid"]
    assert response["booking"]["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"]
    assert response["booking"]["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"]
    assert response["booking"]["additionalneeds"] == booking_data["additionalneeds"]


@allure.feature("Create booking")
@allure.story("Positive: Create booking with random data")
def test_create_booking_with_random_data(api_client, generate_random_booking_data):
    booking_data = generate_random_booking_data

    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f"Response validation error: {e}")

    assert response["booking"]["firstname"] == booking_data["firstname"]
    assert response["booking"]["lastname"] == booking_data["lastname"]
    assert response["booking"]["totalprice"] == booking_data["totalprice"]
    assert response["booking"]["depositpaid"] == booking_data["depositpaid"]
    assert response["booking"]["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"]
    assert response["booking"]["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"]
    assert response["booking"]["additionalneeds"] == booking_data["additionalneeds"]


@allure.feature("Create booking")
@allure.story("Positive: Create booking without additionalneeds")
def test_create_booking_without_additional_needs(api_client):
    booking_data = {
        "firstname": "Nikolay",
        "lastname": "Zhuravlev",
        "totalprice": 250,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-04-20",
            "checkout": "2026-04-23"
        }
    }

    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f"Response validation error: {e}")

    assert "additionalneeds" not in response["booking"]


@allure.feature("Create booking")
@allure.story("Negative: creating booking with empty data")
def test_create_booking_with_empty_data(api_client):
    booking_data = {}

    with pytest.raises(requests.exceptions.HTTPError) as exc:
        api_client.create_booking(booking_data)

    response = exc.value.response

    assert response.status_code == 500, f"Expected status code 500, but got {response.status_code}"
    assert response.text == "Internal Server Error", f"Expected error text Internal Server Error, but got {response.text}"


@allure.feature("Create booking")
@allure.story("Negative: creating booking without firstname")
def test_create_booking_without_firstname(api_client, booking_dates):
    booking_data = {
        "lastname": "Zhuravlev",
        "totalprice": 250,
        "depositpaid": True,
        "bookingdates": booking_dates
    }

    with pytest.raises(requests.exceptions.HTTPError) as exc:
        api_client.create_booking(booking_data)

    response = exc.value.response

    assert response.status_code == 500, f"Expected status code 500, but got {response.status_code}"
    assert response.text == "Internal Server Error", f"Expected error text Internal Server Error, but got {response.text}"


@allure.feature("Create booking")
@allure.story("Negative: creating booking without lastname")
def test_create_booking_without_lastname(api_client, booking_dates):
    booking_data = {
        "firstname": "Nikolay",
        "totalprice": 250,
        "depositpaid": True,
        "bookingdates": booking_dates
    }

    with pytest.raises(requests.exceptions.HTTPError) as exc:
        api_client.create_booking(booking_data)

    response = exc.value.response

    assert response.status_code == 500, f"Expected status code 500, but got {response.status_code}"
    assert response.text == "Internal Server Error", f"Expected error text Internal Server Error, but got {response.text}"


@allure.feature("Create booking")
@allure.story("Negative: creating booking without totalprice")
def test_create_booking_without_totalprice(api_client, booking_dates):
    booking_data = {
        "firstname": "Nikolay",
        "lastname": "Zhuravlev",
        "depositpaid": True,
        "bookingdates": booking_dates
    }

    with pytest.raises(requests.exceptions.HTTPError) as exc:
        api_client.create_booking(booking_data)

    response = exc.value.response

    assert response.status_code == 500, f"Expected status code 500, but got {response.status_code}"
    assert response.text == "Internal Server Error", f"Expected error text Internal Server Error, but got {response.text}"


@allure.feature("Create booking")
@allure.story("Negative: creating booking without depositpaid")
def test_create_booking_without_depositpaid(api_client, booking_dates):
    booking_data = {
        "firstname": "Nikolay",
        "lastname": "Zhuravlev",
        "totalprice": 250,
        "bookingdates": booking_dates
    }

    with pytest.raises(requests.exceptions.HTTPError) as exc:
        api_client.create_booking(booking_data)

    response = exc.value.response

    assert response.status_code == 500, f"Expected status code 500, but got {response.status_code}"
    assert response.text == "Internal Server Error", f"Expected error text Internal Server Error, but got {response.text}"


@allure.feature("Create booking")
@allure.story("Negative: creating booking without bookingdates")
def test_create_booking_without_bookingdates(api_client):
    booking_data = {
        "firstname": "Nikolay",
        "lastname": "Zhuravlev",
        "totalprice": 250,
        "depositpaid": True
    }

    with pytest.raises(requests.exceptions.HTTPError) as exc:
        api_client.create_booking(booking_data)

    response = exc.value.response

    assert response.status_code == 500, f"Expected status code 500, but got {response.status_code}"
    assert response.text == "Internal Server Error", f"Expected error text Internal Server Error, but got {response.text}"


@allure.feature("Create booking")
@allure.story("Negative: creating booking without checkin")
def test_create_booking_without_checkin(api_client):
    booking_data = {
        "firstname": "Nikolay",
        "lastname": "Zhuravlev",
        "totalprice": 250,
        "depositpaid": True,
        "bookingdates": {
            "checkout": "2026-04-23"
        },
        "additionalneeds": "Dinner"
    }

    with pytest.raises(requests.exceptions.HTTPError) as exc:
        api_client.create_booking(booking_data)

    response = exc.value.response

    assert response.status_code == 500, f"Expected status code 500, but got {response.status_code}"
    assert response.text == "Internal Server Error", f"Expected error text Internal Server Error, but got {response.text}"


@allure.feature("Create booking")
@allure.story("Negative: creating booking without checkout")
def test_create_booking_without_checkout(api_client):
    booking_data = {
        "firstname": "Nikolay",
        "lastname": "Zhuravlev",
        "totalprice": 250,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-04-23"
        },
        "additionalneeds": "Dinner"
    }

    with pytest.raises(requests.exceptions.HTTPError) as exc:
        api_client.create_booking(booking_data)

    response = exc.value.response

    assert response.status_code == 500, f"Expected status code 500, but got {response.status_code}"
    assert response.text == "Internal Server Error", f"Expected error text Internal Server Error, but got {response.text}"
