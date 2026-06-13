import math

def display_flights(flights):
    print("----- DANH SÁCH CHUYẾN BAY & HẬU CẦN -----")
    for index, flight in enumerate(flights, start=1):
        water_boxes = math.ceil(flight["passengers"] / 10)
        print(
            f"{index}. Mã: {flight['flight_id']} | "
            f"Khởi hành: {flight['depart_time']} | "
            f"Số khách: {flight['passengers']} | "
            f"Dự phòng: {water_boxes} thùng nước."
        )