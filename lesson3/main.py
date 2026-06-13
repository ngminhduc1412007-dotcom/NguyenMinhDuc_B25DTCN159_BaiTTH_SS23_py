from core.logistics import display_flights
from core.manager import add_flight
from utils.time_helper import calculate_eta
from utils.file_helper import create_folder

flights = [
    {"flight_id": "RA001", "passengers": 154, "depart_time": "2026-06-15 08:00:00", "duration_min": 120}, # Hà Nội - TP.HCM
    {"flight_id": "RA002", "passengers": 85,  "depart_time": "2026-06-15 13:30:00", "duration_min": 45}   # Hà Nội - Vinh
]

def main():
    while True:
        print('''
===== HỆ THỐNG ĐIỀU HÀNH BAY RIKKEI AVIATION =====
1. Hiển thị lịch trình và Thống kê hậu cần
2. Tiếp nhận chuyến bay mới
3. Tính thời gian hạ cánh dự kiến (ETA)
4. Khởi tạo thư mục lưu trữ log hệ thống
5. Thoát chương trình
==================================================
Nhập lựa chọn của bạn:          
            ''')
        try:
            choice = int(input("Nhập lựa chọn của bạn: "))

            match choice:

                case 1:
                    display_flights(flights)

                case 2:
                    add_flight(flights)

                case 3:
                    calculate_eta(flights)

                case 4:
                    create_folder()

                case 5:
                    print("Thoát chương trình ... !")
                    break

                case _:
                    print("Vui lòng nhập từ 1 đến 5!")

        except ValueError:
            print("Vui lòng nhập từ 1 đến 5!")
            
main()