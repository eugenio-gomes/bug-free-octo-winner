import unittest
from emergency_management import Emergency, FireEmergency, Explosion, NaturalDisaster, Earthquake, Storm, EmergencyManager

class TestEmergency(unittest.TestCase):

    def test_emergency_creation(self):
        emergency = Emergency("New York", "reported")
        self.assertEqual(emergency.location, "New York")
        self.assertEqual(emergency.status, "reported")
        self.assertEqual(str(emergency), "Emergency(location=New York, status=reported)")

    def test_fire_emergency(self):
        fire = FireEmergency("California", "high", "in progress")
        self.assertEqual(fire.location, "California")
        self.assertEqual(fire.severity, "high")
        self.assertEqual(fire.status, "in progress")
        self.assertEqual(str(fire), "FireEmergency(location=California, severity=high, status=in progress)")
        fire.update_severity("moderate")
        self.assertEqual(fire.severity, "moderate")

    def test_explosion(self):
        explosion = Explosion("Texas", "high", "reported")
        self.assertEqual(explosion.location, "Texas")
        self.assertEqual(explosion.intensity, "high")
        self.assertEqual(explosion.status, "reported")
        self.assertEqual(str(explosion), "Explosion(location=Texas, intensity=high, status=reported)")
        explosion.update_intensity("moderate")
        self.assertEqual(explosion.intensity, "moderate")

    def test_natural_disaster(self):
        disaster = NaturalDisaster("Florida", 5.0, "Miami", "resolved")
        self.assertEqual(disaster.location, "Florida")
        self.assertEqual(disaster.magnitude, 5.0)
        self.assertEqual(disaster.affected_area, "Miami")
        self.assertEqual(disaster.status, "resolved")
        self.assertEqual(str(disaster), "NaturalDisaster(location=Florida, magnitude=5.0, affected_area=Miami, status=resolved, casualties=0, infrastructure_damage={})")
        disaster.assess_damage("Bridge", 10)
        self.assertEqual(disaster.infrastructure_damage["Bridge"], 10)
        disaster.report_casualties(5)
        self.assertEqual(disaster.casualties, 5)

    def test_earthquake(self):
        earthquake = Earthquake("Japan", 7.8, "Tokyo", "in progress", "35.6895N, 139.6917E")
        self.assertEqual(earthquake.location, "Japan")
        self.assertEqual(earthquake.magnitude, 7.8)
        self.assertEqual(earthquake.affected_area, "Tokyo")
        self.assertEqual(earthquake.status, "in progress")
        self.assertEqual(earthquake.epicenter, "35.6895N, 139.6917E")
        self.assertEqual(str(earthquake), "Earthquake(location=Japan, magnitude=7.8, affected_area=Tokyo, status=in progress, epicenter=35.6895N, 139.6917E, casualties=0, infrastructure_damage={})")
        earthquake.assess_damage("Building", "Severe")
        self.assertEqual(earthquake.infrastructure_damage["Building"], "Severe")

    def test_storm(self):
        storm = Storm("Louisiana", 4.0, "New Orleans", "reported", "Category 4")
        self.assertEqual(storm.location, "Louisiana")
        self.assertEqual(storm.magnitude, 4.0)
        self.assertEqual(storm.affected_area, "New Orleans")
        self.assertEqual(storm.status, "reported")
        self.assertEqual(storm.category, "Category 4")
        self.assertEqual(str(storm), "Storm(location=Louisiana, magnitude=4.0, affected_area=New Orleans, status=reported, category=Category 4, casualties=0, infrastructure_damage={})")
        storm.assess_damage("Levee", "Severe")
        self.assertEqual(storm.infrastructure_damage["Levee"], "Severe")

    def test_emergency_manager(self):
        manager = EmergencyManager()
        fire = FireEmergency("California", "high", "in progress")
        explosion = Explosion("Texas", "high", "reported")
        manager.add_emergency(fire)
        manager.add_emergency(explosion)
        self.assertEqual(len(manager.emergencies), 2)
        self.assertEqual(manager.emergencies[0], fire)
        self.assertEqual(manager.emergencies[1], explosion)

if __name__ == '__main__':
    unittest.main()
