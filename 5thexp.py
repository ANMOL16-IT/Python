class ElectricityReading:
    def __init__(self, meter_id, reading):
        self.meter_id = meter_id
        self.reading = reading
    def display(self):
        print("Meter ID:", self.meter_id, "Consumption:", self.reading, "kWh")
def generate_readings(readings):
    for reading in readings:
        yield reading
class ConsumptionMonitor:
    def __init__(self, readings):
        self.readings = readings

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.readings)
data = [
    ElectricityReading("M101", 120),
    ElectricityReading("M102", 250),
    ElectricityReading("M103", 180),
    ElectricityReading("M104", 320),
    ElectricityReading("M105", 150)
]
readings = generate_readings(data)
monitor = ConsumptionMonitor(readings)
total = 0
count = 0
threshold = 200
print("BESCOM Electricity Consumption Report")
for reading in monitor:
    reading.display()
    total += reading.reading
    count += 1
    if reading.reading > threshold:
        print("Warning: High Consumption")
average = total / count
print("\nConsumption Statistics")
print("----------------------")
print("Total Consumption:", total, "kWh")
print("Average Consumption:", average, "kWh")