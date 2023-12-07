import struct


class ClientInfo:
    def __init__(self, client_id, base_package_months, social_package_months):
        self.client_id = client_id
        self.base_package_months = base_package_months
        self.social_package_months = social_package_months

    def calculate_payment_difference(self):
        base_package_payment = self.base_package_months * base_package_cost
        social_package_payment = self.social_package_months * social_package_cost
        return social_package_payment - base_package_payment


base_package_cost = 30
social_package_cost = 40
clients_data = [
    ClientInfo(1, 12, 6),
    # Пример: клиент оплатил базовый пакет 12 месяцев, затем хочет перейти на социальный на 6 месяцев
]
with open("clients_data.bin", "wb") as file:
    for client in clients_data:
        data = struct.pack("Iii", client.client_id, client.base_package_months, client.social_package_months)
        file.write(data)
for client in clients_data:
    payment_difference = client.calculate_payment_difference()
    print(f"Разница в оплате для клиента {client.client_id}: ${payment_difference}")
