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

