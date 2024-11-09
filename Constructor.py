class employee:
    def __init__(self):
        print("Employee Created")
    def __del__(self):
        print("Employee Deleted")
obj=employee
del obj