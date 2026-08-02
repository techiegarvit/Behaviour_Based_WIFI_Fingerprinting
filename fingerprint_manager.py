import sqlite3

def save_fingerprint(

    ssid,
    rssi,
    latency,
    channel,
    security

):

    conn = sqlite3.connect(
        "fingerprints.db"
    )

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO fingerprints
    (
        ssid,
        avg_rssi,
        avg_latency,
        channel,
        encryption
    )

    VALUES (?, ?, ?, ?, ?)

    """, (

        ssid,
        rssi,
        latency,
        channel,
        security

    ))

    conn.commit()

    conn.close()


def get_fingerprint(ssid):

    conn = sqlite3.connect(
        "fingerprints.db"
    )

    cursor = conn.cursor()

    cursor.execute("""

    SELECT * FROM fingerprints
    WHERE ssid=?

    """, (ssid,))

    data = cursor.fetchone()

    conn.close()

    return data