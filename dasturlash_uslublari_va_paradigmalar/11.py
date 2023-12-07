class Address:
    def __init__(self, user_id, name, status, date, address_id):
        self.user_id = user_id
        self.name = name
        self.status = status
        self.date = date
        self.address_id = address_id

    def display_address(self):
        print(f"User ID: {self.user_id}")
        print(f"Name: {self.name}")
        print(f"Status: {self.status}")
        print(f"Date: {self.date}")
        print(f"Address ID: {self.address_id}")


    def correct_address(self, new_name, new_status):
        print(f"Correcting Address for User ID {self.user_id}...")
        self.name = new_name
        self.status = new_status
        print("Correction successful.")

    def __del__(self):
        print(f"Address object for User ID {self.user_id} has been deleted.")

user_address = Address(user_id=1, name="John Doe", status="Active", date="2023-12-07", address_id=123)
print()
print()
user_address.display_address()
print()
print()
user_address.correct_address(new_name="Jane Doe", new_status="Inactive")
print()
print()
user_address.display_address()
print()
print()
del user_address