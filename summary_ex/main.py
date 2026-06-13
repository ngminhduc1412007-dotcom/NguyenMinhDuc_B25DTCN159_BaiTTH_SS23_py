from hrm_package.ui_display import display_records

from hrm_package.attendance_logic import (clock_in, clock_out)

from hrm_package.time_calc import (evaluate_flex_time as evaluate_shifts)

attendance_book = [
    {"id": "NV01", "name": "Nguyễn Văn A", "times": ("08:30", "17:30")},
    {"id": "NV02", "name": "Trần Thị B", "times": ("09:30", None)}, # Đang làm việc, chưa chấm công ra
    {"id": "NV03", "name": "Lê Văn C", "times": ("10:15", "19:15")}
]
def main():
    while True:
        print('''
=== HỆ THỐNG CHẤM CÔNG RIKKEI (FLEX-TIME) ===
1. Xem bảng chấm công ngày
2. Chấm công Vào (Clock-in)
3. Chấm công Ra (Clock-out)
4. Đánh giá vi phạm
5. Thoát chương trình 
=============================================          
            ''')
        choice = input("Chọn chức năng (1-5): ").strip()
        if not choice.isdigit():
            print("Lua chon khong hop le")
            continue
        choice = int(choice)
        
        match choice:
            case 1:
                display_records(attendance_book)

            case 2:
                clock_in(attendance_book)

            case 3:
                clock_out(attendance_book)

            case 4:
                evaluate_shifts(attendance_book)

            case 5:
                print("Thoát chương trình!")
                break

            case _:
                print("Lựa chọn không hợp lệ!")
                
main()