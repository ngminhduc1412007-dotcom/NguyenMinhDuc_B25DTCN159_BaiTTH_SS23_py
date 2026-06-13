NAME = 'An'

def print_module():
    print("Hello World!")
    
def validate_empty(prompt):
    while True:
        input_data = input(prompt).strip()
        if len(input_data) == 0:
            print("khong duoc nhap trong")
            continue
        else:
            return input_data