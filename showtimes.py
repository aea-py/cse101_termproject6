seat_map_for_show1 = {

    "A1": "available",
    "A2": "available",
    "A3": "available",
    "A4": "available",
    "A5": "available",
    "A6": "available",
    "A7": "available",
    "B1": "available",
    "B2": "available",
    "B3": "available",
    "B4": "available",
    "B5": "available",
    "B6": "available",
    "B7": "available",
    "C1": "available",
    "C2": "available",
    "C3": "available",
    "C4": "available",
    "C5": "available",
    "C6": "available",
    "C7": "available"
}

seat_map_for_show2 = {

    "A1": "available",
    "A2": "available",
    "A3": "available",
    "A4": "available",
    "A5": "available",
    "A6": "available",
    "A7": "available",
    "B1": "available",
    "B2": "available",
    "B3": "available",
    "B4": "available",
    "B5": "available",
    "B6": "available",
    "B7": "available",
    "C1": "available",
    "C2": "available",
    "C3": "available",
    "C4": "available",
    "C5": "available",
    "C6": "available",
    "C7": "available"
}

seat_map_for_show4 = {

    "A1": "available",
    "A2": "available",
    "A3": "available",
    "A4": "available",
    "A5": "available",
    "A6": "available",
    "A7": "available",
    "B1": "available",
    "B2": "available",
    "B3": "available",
    "B4": "available",
    "B5": "available",
    "B6": "available",
    "B7": "available",
    "C1": "available",
    "C2": "available",
    "C3": "available",
    "C4": "available",
    "C5": "available",
    "C6": "available",
    "C7": "available"
}

def is_seat_available(seat_map, seat_number):
    if seat_map[seat_number] == "available":
        return True
    else:
        return False

def reserve_seat(seat_map, seat_number):
    if is_seat_available(seat_map, seat_number):
        seat_map[seat_number] = "reserved"
        return True
    else:
        return False

def release_seat(seat_map, seat_number):
    if seat_map[seat_number] == "reserved":
        seat_map[seat_number] = "available"
        return True
    else:
        return False

