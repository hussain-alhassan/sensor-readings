import time, random
import requests
from datetime import datetime, timezone

sensor_id = 'sensor1'
sensor_type = 'temperature'
while True:
    value = random.randint(-30, 30)
    if value < -20 or value > 15:
        alert = True
    else:
        alert = False

    reading = {
        "id": sensor_id,
        "type": sensor_type,
        "value": value,
        "alert": alert,
        "time_stamp": datetime.now().astimezone(timezone.utc).isoformat(),
    }

    print(f"sending reading: {reading}")
    requests.request("post", "http://127.0.0.1:5000/sensor-readings", json=reading)

    time.sleep(1)