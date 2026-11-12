"""Menu-driven terminal interface for the Oracle PL/SQL project.

Configure ORACLE_USER, ORACLE_PASSWORD, and ORACLE_DSN as environment variables.
"""

import os
import sys

try:
    import oracledb
except ImportError:
    print("Missing dependency. Run: pip install -r requirements.txt")
    sys.exit(1)


def connect():
    user = os.getenv("ORACLE_USER")
    password = os.getenv("ORACLE_PASSWORD")
    dsn = os.getenv("ORACLE_DSN", "localhost:1521/freepdb1")
    if not user or not password:
        raise RuntimeError("Set ORACLE_USER and ORACLE_PASSWORD environment variables.")
    return oracledb.connect(user=user, password=password, dsn=dsn)


def show_events(connection):
    with connection.cursor() as cur:
        cur.execute("""
            SELECT EVENT_ID, EVENT_NAME, EVENT_DATE, PARTICIPANTS
            FROM EVENTS ORDER BY EVENT_ID
        """)
        for row in cur:
            print(row)


def show_venues(connection):
    with connection.cursor() as cur:
        cur.execute("""
            SELECT VENUE_ID, VENUE_NAME, CAPACITY, AVAILABLE
            FROM VENUES ORDER BY VENUE_ID
        """)
        for row in cur:
            print(row)


def calculate_fees(connection):
    with connection.cursor() as cur:
        cur.execute("""
            SELECT EVENT_NAME, PARTICIPANTS,
                   CALCULATE_EVENT_FEE(PARTICIPANTS) AS ESTIMATED_FEE
            FROM EVENTS ORDER BY EVENT_ID
        """)
        for row in cur:
            print(row)


def book_venue(connection):
    booking_id = int(input("Booking ID (unused number): "))
    event_id = int(input("Event ID: "))
    venue_id = int(input("Venue ID: "))
    with connection.cursor() as cur:
        cur.callproc("BOOK_VENUE", [booking_id, event_id, venue_id])


def booking_report(connection):
    with connection.cursor() as cur:
        cur.callproc("DISPLAY_BOOKING_REPORT")


def show_audit(connection):
    with connection.cursor() as cur:
        cur.execute("""
            SELECT AUDIT_ID, BOOKING_ID, OPERATION, MODIFIED_BY, CHANGE_DATE
            FROM BOOKING_AUDIT ORDER BY AUDIT_ID
        """)
        for row in cur:
            print(row)


def main():
    try:
        connection = connect()
    except Exception as exc:
        print(f"Database connection failed: {exc}")
        return

    print("Connected to Oracle Database.")
    actions = {
        "1": ("View All Events", show_events),
        "2": ("View All Venues", show_venues),
        "3": ("Calculate Registration Fees", calculate_fees),
        "4": ("Book a Venue", book_venue),
        "5": ("Display Booking Report", booking_report),
        "6": ("View Booking Audit", show_audit),
    }

    try:
        while True:
            print("\nCAMPUS EVENT AND VENUE MANAGEMENT SYSTEM")
            for key, (label, _) in actions.items():
                print(f"{key}. {label}")
            print("7. Exit")
            choice = input("Enter choice: ").strip()
            if choice == "7":
                break
            if choice not in actions:
                print("Invalid choice. Try again.")
                continue
            try:
                actions[choice][1](connection)
            except Exception as exc:
                print(f"Operation failed: {exc}")
    finally:
        connection.close()
        print("Database connection closed.")


if __name__ == "__main__":
    main()
