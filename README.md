# Campus Event and Venue Management System

A student project demonstrating event discovery, date-based sorting, venue allocation, and database-backed booking management.

This repository contains two related implementations discussed during project development:

- **DAA_Python** — Python/Tkinter application demonstrating searching, sorting, and greedy venue allocation.
- **PLSQL_Database** — Oracle SQL/PLSQL scripts demonstrating relational tables, fee calculation, venue booking validation, cursor-based reporting, and deletion auditing.

## Technologies

- Python 3
- Tkinter (included with most standard Python installations)
- Oracle Database (tested project context: local `freepdb1` service)
- Oracle SQL and PL/SQL
- Python `oracledb` driver for the optional database-connected terminal app

## Repository structure

```text
Campus_Event_Venue_Management/
├── DAA_Python/
│   ├── campus_event_system.py
│   └── README.md
├── PLSQL_Database/
│   ├── 01_create_tables.sql
│   ├── 02_sample_data.sql
│   ├── 03_fee_function.sql
│   ├── 04_booking_procedure.sql
│   ├── 05_booking_report_cursor.sql
│   ├── 06_booking_audit.sql
│   ├── 07_test_queries.sql
│   ├── campus_management.py
│   ├── requirements.txt
│   └── README.md
└── .gitignore
```

## Run the DAA Python application

From the `DAA_Python` folder:

```bash
python campus_event_system.py
```

The application provides:
- View all events
- Search for an event by name
- Sort events by date using Merge Sort
- Allocate a suitable venue using a greedy selection strategy

## Set up the Oracle PL/SQL project

1. Connect to your Oracle pluggable database (for example, `freepdb1`) using SQL Developer or the VS Code Oracle extension.
2. Run the SQL files in numerical order: `01` through `07`.
3. Review the PL/SQL README for the purpose of each script.
4. For the optional Python database menu, install the dependency and configure your connection using environment variables.

Never commit database passwords, private connection strings, or personal credentials.

## Python database app configuration

Set these environment variables before running `campus_management.py`:

- `ORACLE_USER`
- `ORACLE_PASSWORD`
- `ORACLE_DSN` (example format: `localhost:1521/freepdb1`)

Install dependency:

```bash
pip install -r requirements.txt
```

Run:

```bash
python campus_management.py
```

## Important project notes

- The fee function calculates an **estimated total event fee** from participant count using the project's tiered rates.
- The audit trigger records deleted bookings.
- Deleting a booking does not automatically make the venue available again in this implementation; availability must be updated separately.
- The Python Tkinter DAA application and Oracle PL/SQL database application are separate demonstrations of related project functionality.
