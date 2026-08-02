def calculate_risk(

    current_rssi,
    trusted_rssi,

    current_latency,
    trusted_latency,

    current_security,
    trusted_security,

    rssi_variance

):

    risk = 0

    # RSSI Difference
    rssi_diff = abs(
        current_rssi - trusted_rssi
    )

    if rssi_diff > 15:
        risk += 40

    # Latency Difference
    latency_diff = abs(
        current_latency - trusted_latency
    )

    if latency_diff > 20:
        risk += 30

    # Security Difference
    if current_security != trusted_security:
        risk += 30

    # RSSI Variance
    if rssi_variance > 20:
        risk += 20

    # Final Status
    if risk <= 30:
        status = "SAFE"

    elif risk <= 60:
        status = "SUSPICIOUS"

    else:
        status = "HIGH RISK"

    return risk, status