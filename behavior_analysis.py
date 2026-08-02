import subprocess
import re
import statistics
import time

from wifi_scanner import scan_wifi

def get_latency():

    try:

        ping = subprocess.check_output(
            ["ping", "-c", "4", "google.com"]
        ).decode()

        times = re.findall(
            r'time=([0-9.]+)',
            ping
        )

        times = [float(t) for t in times]

        if len(times) == 0:
            return 0

        avg_latency = sum(times) / len(times)

        return round(avg_latency, 2)

    except Exception as e:

        print("Error:", e)

        return 0


def get_rssi_variance():

    rssi_values = []

    for i in range(5):

        wifi = scan_wifi()

        try:

            rssi = int(wifi["rssi"])

            rssi_values.append(rssi)

        except:
            pass

        time.sleep(1)

    if len(rssi_values) < 2:
        return 0

    variance = statistics.variance(rssi_values)

    return round(variance, 2)