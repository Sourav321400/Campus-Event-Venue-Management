# Oracle PL/SQL Database Component

Run the numbered `.sql` scripts in order in your Oracle schema.

## Script order

1. `01_create_tables.sql` — creates EVENTS, VENUES, BOOKINGS, and BOOKING_AUDIT.
2. `02_sample_data.sql` — inserts the four sample events and four venues.
3. `03_fee_function.sql` — creates `CALCULATE_EVENT_FEE`.
4. `04_booking_procedure.sql` — creates `BOOK_VENUE`.
5. `05_booking_report_cursor.sql` — creates `DISPLAY_BOOKING_REPORT`.
6. `06_booking_audit.sql` — creates the audit sequence and delete trigger.
7. `07_test_queries.sql` — example calls and verification queries.

Run scripts using a schema where you have permission to create tables, sequences, procedures, functions, and triggers. If an object already exists, remove or rename it before rerunning its creation script.

## Main PL/SQL concepts

- Function: calculates estimated event fee by participant count.
- Procedure: validates capacity and availability, then books a venue.
- Explicit cursor: displays booking information row by row.
- Trigger: records deleted booking information in the audit table.

## Python terminal application

`campus_management.py` connects to Oracle using the `oracledb` package. Configure credentials through environment variables; do not hard-code or commit passwords.
