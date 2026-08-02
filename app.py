from flask import Flask, render_template

from wifi_scanner import scan_wifi
from behavior_analysis import (
    get_latency,
    get_rssi_variance
)

from fingerprint_manager import (
    save_fingerprint,
    get_fingerprint
)

from anomaly_detection import calculate_risk

app = Flask(__name__)

@app.route("/")

def home():

    wifi_data = scan_wifi()

    latency = get_latency()

    rssi_variance = get_rssi_variance()

    ssid = wifi_data["ssid"]

    current_rssi = int(wifi_data["rssi"])

    current_security = wifi_data["security"]

    channel = wifi_data["channel"]

    trusted = get_fingerprint(ssid)

    if trusted is None:

        save_fingerprint(
            ssid,
            current_rssi,
            latency,
            channel,
            current_security
        )

        risk = 0

        status = "TRUSTED"

    else:

        trusted_rssi = trusted[2]

        trusted_latency = trusted[3]

        trusted_security = trusted[5]

        risk, status = calculate_risk(
            current_rssi,
            trusted_rssi,
            latency,
            trusted_latency,
            current_security,
            trusted_security,
            rssi_variance
        )

    return render_template(
        "index.html",
        wifi_data=wifi_data,
        latency=latency,
        rssi_variance=rssi_variance,
        risk=risk,
        status=status
    )

if __name__ == "__main__":

    app.run(debug=True)