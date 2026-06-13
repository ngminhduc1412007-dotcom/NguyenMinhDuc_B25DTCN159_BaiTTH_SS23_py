def clock_in(attendance_book):

    employee_id = input("Nhập mã nhân viên: ")
    employee_name = input("Nhập tên nhân viên: ")
    clock_in_time = input("Nhập giờ vào (HH:MM): ")

    for employee in attendance_book:
        if employee["id"] == employee_id:
            print("Mã nhân viên đã tồn tại!")
            return

    attendance_book.append(
        {
            "id": employee_id,
            "name": employee_name,
            "times": (clock_in_time, None)
        }
    )

    print(f"Thành công: Đã ghi nhận {employee_id} chấm công vào lúc {clock_in_time}!")

def clock_out(attendance_book):
    employee_id = input("Nhập mã nhân viên: ")
    clock_out_time = input("Nhập giờ ra (HH:MM): ")
    for employee in attendance_book:
        if employee["id"] == employee_id:
            old_clock_in = employee["times"][0]
            employee["times"] = (old_clock_in, clock_out_time)
            print("Chấm công ra thành công!")
            return
    print("Không tìm thấy nhân viên!")