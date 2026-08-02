import subprocess
import re

def scan_wifi():

    command = [
        "system_profiler",
        "SPAirPortDataType"
    ]

    result = subprocess.check_output(command).decode("utf-8")

    ssid = "Unknown"
    channel = "Unknown"
    security = "Unknown"
    rssi = "-60"

    ssid_match = re.search(
        r'Current Network Information:\\s+(.+?):',
        result
    )

    if ssid_match:
        ssid = ssid_match.group(1)

    channel_match = re.search(
        r'Channel: (.+)',
        result
    )

    if channel_match:
        channel = channel_match.group(1)

    security_match = re.search(
        r'Security: (.+)',
        result
    )

    if security_match:
        security = security_match.group(1)

    signal_match = re.search(
        r'Signal / Noise: (-?\\d+)',
        result
    )

    if signal_match:
        rssi = signal_match.group(1)

    return {

        "ssid": ssid,

        "channel": channel,

        "security": security,

        "rssi": rssi

    }