
def flight_itenarary(flight_lists):
    for i, flights in enumerate(flight_lists, 1):
        name, origin, destination= flights
        print(f"Itenarary {i}: {name} is departing from {origin} traveling to {destination}." , )

def get_itineraries():
    flight_list = []
    while True:
        traveler_name = input("Enter traveler name (or 'done' to finish): ")
        if traveler_name.lower() == 'done':
            break
        origin = input("Enter origin: ")
        destination = input("Enter destination: ")
        flight_list.append((traveler_name, origin, destination))
    
    return flight_list


flight_list = get_itineraries()
print(f"\nCollected Flight Itineraries: {flight_list}")

flight_itenarary(flight_list)