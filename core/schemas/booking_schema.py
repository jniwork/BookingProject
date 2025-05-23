BOOKING_SCHEMA = {
    "type": "object",
    "properties": {
        "bookingid": {"type": "integer"},
        "booking": {
            "type": "object",
            "properties": {
                "firstname": {"type": "string"},
                "lastname": {"type": "string"},
                "totalprice": {"type": "integer"},
                "depositpaid": {"type": "boolean"},
                "bookingdates": {
                    "type": "object",
                    "properties": {
                        "checkin": {"type": "string", "format": "date"},
                        "checkout": {"type": "string", "format": "date"}
                    }
                },
                "additionalneeds": {"type": "string"}
            }
        }
    }
}
