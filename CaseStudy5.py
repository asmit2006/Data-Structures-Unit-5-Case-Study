"""
Case Study: GPS/Navigation System Using a Weighted Graph

The city is represented as a weighted, undirected graph:
- Vertices represent locations.
- Edges represent roads.
- Edge weights represent travel distance.

Dijkstra's algorithm finds a shortest-distance route between two locations.
This is an educational console simulation, not a live GPS service.
"""

import heapq


class CityMap:
    def __init__(self):
        self.graph = {}

    def add_location(self, name):
        name = name.strip()
        if name:
            self.graph.setdefault(name, {})

    def add_road(self, location_a, location_b, distance):
        location_a = location_a.strip()
        location_b = location_b.strip()
        if not location_a or not location_b:
            raise ValueError("Location names cannot be empty.")
        if distance <= 0:
            raise ValueError("Road distance must be greater than zero.")

        self.add_location(location_a)
        self.add_location(location_b)
        self.graph[location_a][location_b] = float(distance)
        self.graph[location_b][location_a] = float(distance)

    def shortest_path(self, start, destination):
        """Return (path, distance), or ([], infinity) if unreachable."""
        if start not in self.graph or destination not in self.graph:
            return [], float("inf")

        distances = {location: float("inf") for location in self.graph}
        previous = {}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current = heapq.heappop(priority_queue)
            if current_distance != distances[current]:
                continue
            if current == destination:
                break

            for neighbor, weight in self.graph[current].items():
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current
                    heapq.heappush(priority_queue, (new_distance, neighbor))

        if distances[destination] == float("inf"):
            return [], float("inf")

        path = []
        current = destination
        while current != start:
            path.append(current)
            current = previous[current]
        path.append(start)
        path.reverse()
        return path, distances[destination]

    def display_map(self):
        if not self.graph:
            print("No locations have been added.")
            return
        print("\n--- City Map (roads and distances) ---")
        for location in sorted(self.graph):
            roads = self.graph[location]
            if roads:
                details = ", ".join(
                    f"{neighbor} ({distance:g} km)"
                    for neighbor, distance in sorted(roads.items())
                )
            else:
                details = "No connected roads"
            print(f"{location}: {details}")


def build_sample_map():
    city = CityMap()
    roads = [
        ("Central Station", "City Hospital", 4),
        ("Central Station", "City Mall", 3),
        ("City Mall", "City Hospital", 2),
        ("City Mall", "University", 5),
        ("City Hospital", "University", 4),
        ("University", "Airport", 8),
        ("City Hospital", "Airport", 15),
        ("City Mall", "Bus Terminal", 4),
        ("Bus Terminal", "Airport", 10),
    ]
    for a, b, distance in roads:
        city.add_road(a, b, distance)
    return city


def main():
    city = build_sample_map()
    print("Sample city map loaded.")
    while True:
        print("\n===== GPS / NAVIGATION DEMO =====")
        print("1. Display city map")
        print("2. Find shortest route")
        print("3. Add a location")
        print("4. Add/update a road")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            city.display_map()
        elif choice == "2":
            start = input("Start location (exact name): ").strip()
            destination = input("Destination (exact name): ").strip()
            path, distance = city.shortest_path(start, destination)
            if not path:
                print("Route unavailable. Check the location names or road connections.")
            else:
                print("Shortest route: " + " -> ".join(path))
                print(f"Total distance: {distance:g} km")
        elif choice == "3":
            name = input("Enter location name: ").strip()
            if not name:
                print("Location name cannot be empty.")
            else:
                city.add_location(name)
                print(f"Location '{name}' added.")
        elif choice == "4":
            a = input("First location: ").strip()
            b = input("Second location: ").strip()
            try:
                distance = float(input("Road distance in km: "))
                city.add_road(a, b, distance)
                print("Road added/updated.")
            except ValueError as exc:
                print(f"Error: {exc}")
        elif choice == "5":
            print("Exiting navigation demo. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
