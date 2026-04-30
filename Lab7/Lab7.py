class Vehicle:
    def __init__(self, vid, model, year):
        self.vid = vid
        self.model = model
        self.year = year

    def __eq__(self, other):
        return self.vid == other.vid

    def is_new(self, n):
        return self.year >= (2026 - n)


class Car(Vehicle):
    def __init__(self, vid, model, year, fuel_type, doors):
        super().__init__(vid, model, year)
        self.fuel_type = fuel_type
        self.doors = doors

    def __str__(self):
        return f"[Car] VID: {self.vid} | {self.model} ({self.year}) | Fuel: {self.fuel_type} | {self.doors} Doors"


class Truck(Vehicle):
    def __init__(self, vid, model, year, max_load, axles):
        super().__init__(vid, model, year)
        self.max_load = max_load
        self.axles = axles

    def __str__(self):
        return f"[Truck] VID: {self.vid} | {self.model} ({self.year}) | Load: {self.max_load}kg | {self.axles} Axles"


class Motorcycle(Vehicle):
    def __init__(self, vid, model, year, engine_cc, mtype):
        super().__init__(vid, model, year)
        self.engine_cc = engine_cc
        self.mtype = mtype

    def __str__(self):
        return f"[Motorcycle] VID: {self.vid} | {self.model} ({self.year}) | Eng: {self.engine_cc}cc | Type: {self.mtype}"


def save_fleet_to_string(vehicles):
    lines = []
    for v in vehicles:
        if isinstance(v, Car):
            lines.append(f"Car,{v.vid},{v.model},{v.year},{v.fuel_type},{v.doors}")
        elif isinstance(v, Truck):
            lines.append(f"Truck,{v.vid},{v.model},{v.year},{v.max_load},{v.axles}")
        elif isinstance(v, Motorcycle):
            lines.append(f"Motorcycle,{v.vid},{v.model},{v.year},{v.engine_cc},{v.mtype}")
    return "\n".join(lines)


def load_fleet_from_string(data):
    vehicles = []
    for line in data.split("\n"):
        parts = line.split(",")

        if parts[0] == "Car":
            v = Car(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5]))
        elif parts[0] == "Truck":
            v = Truck(parts[1], parts[2], int(parts[3]), int(parts[4]), int(parts[5]))
        elif parts[0] == "Motorcycle":
            v = Motorcycle(parts[1], parts[2], int(parts[3]), int(parts[4]), parts[5])

        vehicles.append(v)

    return vehicles


vehicles = [
    Car("V001", "Tesla Model 3", 2023, "Electric", 4),
    Car("V002", "Toyota Corolla", 2018, "Petrol", 4),
    Truck("T101", "Volvo FH16", 2019, 25000, 6),
    Truck("T102", "Mercedes Actros", 2021, 18000, 4),
    Motorcycle("M301", "Yamaha R1", 2024, 998, "Sport"),
    Motorcycle("M302", "Harley Davidson", 2015, 1200, "Cruiser")
]


data = save_fleet_to_string(vehicles)


print("Loading fleet data...")
loaded_vehicles = load_fleet_from_string(data)
print(f"{len(loaded_vehicles)} vehicles loaded successfully.\n")


print("--- All Vehicles ---")
for v in loaded_vehicles:
    print(v)


print("\n--- Recent Vehicles (Last 4 Years) ---")
for v in loaded_vehicles:
    if v.is_new(4):
        print(v)


print("\n--- Electric Cars Only ---")
for v in loaded_vehicles:
    if isinstance(v, Car) and v.fuel_type == "Electric":
        print(v)
