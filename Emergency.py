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


# Example usage with user input
location = input("Enter the location of the fire: ")
severity = input("Enter the severity of the fire (low, moderate, high): ")
status = input("Enter the status of the emergency (reported, in progress, resolved): ")

fire = FireEmergency(location, severity, status)
print(fire)


class Explosion(FireEmergency):
    def __init__(self, location, intensity, status):
        super().__init__(location, "high", status)  # Setting severity to 'high' for explosions
        self.intensity = intensity

    def update_intensity(self, new_intensity):
        self.intensity = new_intensity
        print(f"Intensity updated to {self.intensity}")

    def __str__(self):
        return f"Explosion(location={self.location}, intensity={self.intensity}, status={self.status})"
# Example usage with user input
location = input("Enter the location of the explosion: ")
intensity = input("Enter the intensity of the explosion (low, moderate, high): ")
status = input("Enter the status of the explosion (reported, in progress, resolved): ")

explosion = Explosion(location, intensity, status)
print(explosion)

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

    # Override the assess_damage method for specific behavior in earthquakes
    def assess_damage(self, infrastructure, damage_level):
        if damage_level == "Severe":
            print(f"Earthquake caused severe damage to {infrastructure}.")
        else:
            super().assess_damage(infrastructure, damage_level)


# Function to create an Earthquake object with user input
def create_earthquake_from_input():
    location = input("Enter the location of the earthquake: ")
    magnitude = float(input("Enter the magnitude of the earthquake: "))
    affected_area = input("Enter the affected area by the earthquake: ")
    status = input("Enter the status of the earthquake (reported, in progress, resolved): ")
    epicenter = input("Enter the epicenter coordinates of the earthquake: ")

    return Earthquake(location, magnitude, affected_area, status, epicenter)

def main():
    earthquake = create_earthquake_from_input()
    print(earthquake)


if __name__ == '__main__':
    main()
