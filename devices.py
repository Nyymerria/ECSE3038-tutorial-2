readings = [
    {"name": "front-door", "room": "hall", "temp": 27.4, "online": True},
    {"name": "hall-lamp", "room": "hall", "temp": 26.1, "online": True},
    {"name": "attic", "room": "attic", "temp": 31.9, "online": True},
    {"name": "fridge", "room": "kitchen", "temp": 4.2, "online": False},
    {"name": "patio", "room": "outside", "temp": 29.8, "online": True},
]

def list_devices(devices):
    for device in devices:
        print(f"Device: {device['name']}, Temperature: {device['temp']}°C",)


list_devices(readings)


def average_temp(devices):
    
    
    total_temp = sum(device['temp'] for device in devices)
    return total_temp / len(devices)


print("\nAverage Temperature ")
avg = average_temp(readings)
print(f"Average: {avg:.2f}°C")

def hottest(readings):
   return max(readings, key=lambda device: device['temp'])


print("\n Hottest Device ")
hottest_device = hottest(readings)
print(hottest_device)

    
