class FireEmergency:
    def __init__(self, location, severity, status):
        self.location = location
        self.severity = severity
        self.status = status

    def update_status(self, new_status):
        self.status = new_status
        print(f"Status updated to {self.status}")

    def update_severity(self, new_severity):
        self.severity = new_severity
        print(f"Severity updated to {self.severity}")

    def __str__(self):
        return f"FireEmergency(location={self.location}, severity={self.severity}, status={self.status})"


class Explosion(FireEmergency):
    def __init__(self, location, intensity, status):
        super().__init__(location, "high", status)  # Setting severity to 'high' for explosions
        self.intensity = intensity

    def update_intensity(self, new_intensity):
        self.intensity = new_intensity
        print(f"Intensity updated to {self.intensity}")

    def __str__(self):
        return f"Explosion(location={self.location}, intensity={self.intensity}, status={self.status})"


class NaturalDisaster:
    def __init__(self, location, magnitude, affected_area, status):
        self.location = location
        self.magnitude = magnitude
        self.affected_area = affected_area
        self.status = status
        self.casualties = 0
        self.infrastructure_damage = {}

    def update_status(self, new_status):
        self.status = new_status
        print(f"Status updated to {self.status}")

    def assess_damage(self, infrastructure, damage_level):
        self.infrastructure_damage[infrastructure] = damage_level
        print(f"{infrastructure} damage assessed as {damage_level}")

    def report_casualties(self, num_casualties):
        self.casualties += num_casualties
        print(f"{num_casualties} casualties reported. Total casualties: {self.casualties}")

    def estimate_economic_impact(self):
        total_damage = sum(self.infrastructure_damage.values())
        print(f"Estimated economic impact: {total_damage} million dollars")

    def __str__(self):
        return f"NaturalDisaster(location={self.location}, magnitude={self.magnitude}, affected_area={self.affected_area}, status={self.status}, casualties={self.casualties}, infrastructure_damage={self.infrastructure_damage})"


class Earthquake(NaturalDisaster):
    def __init__(self, location, magnitude, affected_area, status, epicenter):
        super().__init__(location, magnitude, affected_area, status)
        self.epicenter = epicenter

    def report_epicenter(self):
        print(f"Earthquake epicenter: {self.epicenter}")

    def assess_damage(self, infrastructure, damage_level):
        if damage_level == "Severe":
            print(f"Earthquake caused severe damage to {infrastructure}.")
        else:
            super().assess_damage(infrastructure, damage_level)

    def __str__(self):
        return (f"Earthquake(location={self.location}, magnitude={self.magnitude}, affected_area={self.affected_area}, status={self.status}, "
                f"epicenter={self.epicenter}, casualties={self.casualties}, infrastructure_damage={self.infrastructure_damage})")


class Storm(NaturalDisaster):
    def __init__(self, location, magnitude, affected_area, status, category):
        super().__init__(location, magnitude, affected_area, status)
        self.category = category

    def report_category(self):
        print(f"Storm category: {self.category}")

    def assess_damage(self, infrastructure, damage_level):
        if damage_level == "Severe":
            print(f"Storm caused severe damage to {infrastructure}.")
        else:
            super().assess_damage(infrastructure, damage_level)

    def __str__(self):
        return (f"Storm(location={self.location}, magnitude={self.magnitude}, affected_area={self.affected_area}, status={self.status}, "
                f"category={self.category}, casualties={self.casualties}, infrastructure_damage={self.infrastructure_damage})")


# Function to create emergencies from user input
def create_earthquake_from_input():
    location = input("Enter the location of the earthquake: ")
    magnitude = float(input("Enter the magnitude of the earthquake: "))
    affected_area = input("Enter the affected area by the earthquake: ")
    status = input("Enter the status of the earthquake (reported, in progress, resolved): ")
    epicenter = input("Enter the epicenter coordinates of the earthquake: ")
    return Earthquake(location, magnitude, affected_area, status, epicenter)


def create_storm_from_input():
    location = input("Enter the location of the storm: ")
    magnitude = float(input("Enter the magnitude of the storm: "))
    affected_area = input("Enter the affected area by the storm: ")
    status = input("Enter the status of the storm (reported, in progress, resolved): ")
    category = input("Enter the category of the storm (e.g., Category 1, Category 2): ")
    return Storm(location, magnitude, affected_area, status, category)


def create_fire_emergency_from_input():
    location = input("Enter the location of the fire: ")
    severity = input("Enter the severity of the fire (low, moderate, high): ")
    status = input("Enter the status of the emergency (reported, in progress, resolved): ")
    return FireEmergency(location, severity, status)


def create_explosion_from_input():
    location = input("Enter the location of the explosion: ")
    intensity = input("Enter the intensity of the explosion (low, moderate, high): ")
    status = input("Enter the status of the explosion (reported, in progress, resolved): ")
    return Explosion(location, intensity, status)


class EmergencyManager:
    def __init__(self):
        self.emergencies = []

    def add_emergency(self, emergency):
        self.emergencies.append(emergency)

    def list_emergencies(self):
        for i, emergency in enumerate(self.emergencies, 1):
            print(f"{i}. {emergency}")

    def select_emergency(self):
        if not self.emergencies:
            print("No emergencies recorded.")
            return None
        self.list_emergencies()
        choice = int(input("Select the emergency number you want to address: "))
        if 1 <= choice <= len(self.emergencies):
            return self.emergencies[choice - 1]
        else:
            print("Invalid choice.")
            return None


def main():
    emergency_manager = EmergencyManager()

    while True:
        print("\n1. Add Fire Emergency")
        print("2. Add Explosion")
        print("3. Add Earthquake")
        print("4. Add Storm")
        print("5. List Emergencies")
        print("6. Select and Update Emergency")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            fire_emergency = create_fire_emergency_from_input()
            emergency_manager.add_emergency(fire_emergency)
        elif choice == '2':
            explosion = create_explosion_from_input()
            emergency_manager.add_emergency(explosion)
        elif choice == '3':
            earthquake = create_earthquake_from_input()
            emergency_manager.add_emergency(earthquake)
        elif choice == '4':
            storm = create_storm_from_input()
            emergency_manager.add_emergency(storm)
        elif choice == '5':
            emergency_manager.list_emergencies()
        elif choice == '6':
            emergency = emergency_manager.select_emergency()
            if emergency:
                new_status = input("Enter new status: ")
                emergency.update_status(new_status)
        elif choice == '7':
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == '__main__':
    main()
