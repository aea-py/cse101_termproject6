import uuid

bookings = []

def create_booking(showtimes, seat_maps, booking_data):
    booked_seats = []

    for seat_number in booking_data["seat_numbers"]:
        if seat_maps[booking_data["showtime"]][seat_number] == "available":
            seat_maps[booking_data["showtime"]][seat_number] = "reserved"
            booked_seats.append(seat_number)
        else:
            print(f"Seat {seat_number} is already reserved.")

    booking = {
        "id": str(uuid.uuid4()),
        "movie": booking_data["movie"],
        "showtime": booking_data["showtime"],
        "seat_numbers": booked_seats,
        "customer_name": booking_data["customer_name"]
    }

    bookings.append(booking)
    return booking

def cancel_booking(bookings: list, booking_id: str, seat_maps: dict) -> bool:

    for booking in bookings:
        if booking["id"] == booking_id:
            # Release each reserved seat
            for seat_number in booking["seat_numbers"]:
                seat_maps[booking["showtime"]][seat_number] = "available"
            # Remove booking from list
            bookings.remove(booking)
            return True
    return False
