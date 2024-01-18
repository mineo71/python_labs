import random
# from test import *

class TransportVehicle:
    def __init__(self, name, capacity, speed):
        self.name = name
        self.capacity = capacity
        self.speed = speed

    def deliver_order(self, order):
        time_required = order['order_distance'] / self.speed
        print(f"{self.name} привезе замовлення {order['order_name']} через {time_required:.2f} годин.")

class Truck(TransportVehicle):
    def __init__(self, name, capacity, speed, order_type):
        super().__init__(name, capacity, speed)
        self.order_type = order_type

    def deliver_order(self, order):
        if order['order_type'] == self.order_type:
            super().deliver_order(order)
        else:
            print(f"{self.name} Не зможе привезти замовлення {order['order_id']} через непідходящий вантаж.")

class Drone(TransportVehicle):
    def __init__(self, name, capacity, speed, max_distance, order_type):
        super().__init__(name, capacity, speed)
        self.max_distance = max_distance
        self.order_type = order_type

    def deliver_order(self, order):
        if order['order_distance'] <= self.max_distance:
            super().deliver_order(order)
        elif order['order_type'] == self.order_type:
            super().deliver_order(order)
        else:
            print(f"{self.name} не зможе привезти замовлення {order['order_id']}.")

class Bicycle(TransportVehicle):
    def __init__(self, name,capacity, speed, order_type):
        super().__init__(name, capacity, speed)
        self.order_type = order_type

    def deliver_order(self, order):
        if order['order_type'] == self.order_type:
            super().deliver_order(order)
        else:
            print(f"{self.name} не зможе привезти замовлення {order['order_id']}.")
            
def delivery_schedule_generator(orders, vehicles):
    schedule = []
    for order in orders:
        available_vehicles = [vehicle for vehicle in vehicles if vehicle.capacity >= order['order_mass'] and vehicle.order_type == order['order_type']]
        if not available_vehicles:
            print(f"Немає вільного транспорту для замовлення {order['order_name']}.")
            continue

        selected_vehicle = random.choice(available_vehicles)
        schedule.append({'order': order, 'vehicle': selected_vehicle})
    return schedule


truck1 = Truck("Scania Ігора", capacity=50, speed=80, order_type="Fragile")
truck2 = Truck("MAN Міші", capacity=30, speed=100, order_type="")
drone1 = Drone("Дрон Влада", capacity=3, speed=30, max_distance=100, order_type="Military")
drone2 = Drone("Дрон Макса", capacity= 20, speed=30, max_distance=300, order_type="Military")
bicycle1 = Bicycle("Велосипед Олега",capacity=10, speed=15, order_type="Food")

orders = [
    {'order_id': 1, 'order_name': "Одяг", 'order_mass': 5, 'order_distance': 450,'order_type': ''},
    {'order_id': 2, 'order_name': "Фарба для волосся", 'order_mass': 2, 'order_distance': 120, 'order_type': 'Food'},
    {'order_id': 3, 'order_name': "Бронижилет", 'order_mass': 30, 'order_distance': 200, 'order_type': 'Military'},
    {'order_id': 4, 'order_name': "Суші набір", 'order_mass': 3, 'order_distance': 50, 'order_type': ''},
    {'order_id': 5, 'order_name': "Медикаменти", 'order_mass': 1, 'order_distance': 30, 'order_type': 'Military'},
    {'order_id': 6, 'order_name': "Шампанське", 'order_mass': 4, 'order_distance': 150, 'order_type': 'Food'},
    {'order_id': 7, 'order_name': "Стіклянні вази", 'order_mass': 6, 'order_distance': 100, 'order_type': 'Fragile'},
    {'order_id': 8, 'order_name': "Ліки", 'order_mass': 1, 'order_distance': 40, 'order_type': ''},
    {'order_id': 9, 'order_name': "Фруктовий салат", 'order_mass': 2, 'order_distance': 60, 'order_type': 'Food'},
    {'order_id': 10, 'order_name': "Бронзова статуя", 'order_mass': 12, 'order_distance': 180, 'order_type': 'Fragile'},
]

vehicles = [truck1, truck2, drone1, drone2, bicycle1]

schedule_generator = delivery_schedule_generator(orders, vehicles)

for delivery in schedule_generator:
    delivery['vehicle'].deliver_order(delivery['order'])

#shedul_generator = open_transport()
