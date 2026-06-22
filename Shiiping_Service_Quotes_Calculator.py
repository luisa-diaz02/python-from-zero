
# PROJECT WEEK 1: SHIPPIG SERVICES QUOTES CALCULATOR

customer_name = input("CUSTOMER NAME: ")
techical_service = input("REQUESTED SERVICE: ")
base_cost = float(input("BASE COST: "))
distance = float(input("DISTANCES PER KM: "))

charge_per_km = 2.5

travel_cost = distance * charge_per_km
total_cost = base_cost + travel_cost

print("|============================================|")
print("|  SHIPPING AND SERVICES QUOTES CALCULATOR   |")
print("|============================================|")

print(f"\nCUSTOMER CLIENT: {customer_name.title().strip()}")
print(f"Requested Service: {techical_service.strip()}")
print(f"BASE COST: {base_cost:.2f} USD. ")
print(f"DISTANCES: {distance} KM ")
print(f"TRAVEL COST: {travel_cost:.2f} USD. ")
print(f"\nTOTAL COST: {total_cost:.2f} USD. ")

print("\n|============================================|")
print("|Status: Pending                             |")
print("|Date: __/__/____                            |")
print("|============================================|")
