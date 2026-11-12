"""Campus Event and Venue Management System - DAA demonstration.

Demonstrates Binary Search, Merge Sort, and greedy venue allocation.
Run with: python campus_event_system.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

EVENTS = [
    {"id": 1, "name": "AI Workshop", "date": "2026-11-05", "participants": 40},
    {"id": 2, "name": "Cultural Fest", "date": "2026-11-12", "participants": 150},
    {"id": 3, "name": "Coding Competition", "date": "2026-11-08", "participants": 80},
    {"id": 4, "name": "Tech Seminar", "date": "2026-11-03", "participants": 50},
]

VENUES = [
    {"id": 101, "name": "Seminar Hall", "capacity": 60, "available": True},
    {"id": 102, "name": "Computer Lab", "capacity": 100, "available": True},
    {"id": 103, "name": "Auditorium", "capacity": 200, "available": True},
    {"id": 104, "name": "Conference Room", "capacity": 45, "available": True},
]

BOOKINGS = []


def merge_sort(items, key):
    """Return a new list sorted by key using Merge Sort."""
    if len(items) <= 1:
        return items[:]
    middle = len(items) // 2
    left = merge_sort(items[:middle], key)
    right = merge_sort(items[middle:], key)
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def binary_search_event(events, target):
    """Find an event by name using Binary Search on a name-sorted list."""
    ordered = sorted(events, key=lambda event: event["name"].casefold())
    low, high = 0, len(ordered) - 1
    target = target.casefold()
    while low <= high:
        mid = (low + high) // 2
        current = ordered[mid]["name"].casefold()
        if current == target:
            return ordered[mid]
        if current < target:
            low = mid + 1
        else:
            high = mid - 1
    return None


def greedy_allocate_venue(participants):
    """Choose the smallest available venue that can fit the participants."""
    suitable = [
        venue for venue in VENUES
        if venue["available"] and venue["capacity"] >= participants
    ]
    if not suitable:
        return None
    return min(suitable, key=lambda venue: venue["capacity"])


class CampusEventApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Campus Event and Venue Management System")
        self.root.geometry("900x580")
        self.root.minsize(760, 500)
        self.build_ui()
        self.refresh_events()
        self.refresh_venues()

    def build_ui(self):
        title = ttk.Label(
            self.root, text="Campus Event and Venue Management System",
            font=("Segoe UI", 17, "bold")
        )
        title.pack(pady=(15, 5))
        subtitle = ttk.Label(
            self.root, text="DAA Demonstration: Binary Search • Merge Sort • Greedy Allocation"
        )
        subtitle.pack(pady=(0, 12))

        controls = ttk.Frame(self.root, padding=8)
        controls.pack(fill="x")

        ttk.Button(controls, text="Show All Events", command=self.refresh_events).pack(side="left", padx=4)
        ttk.Button(controls, text="Sort by Date", command=self.sort_events).pack(side="left", padx=4)

        ttk.Label(controls, text="Event name:").pack(side="left", padx=(18, 4))
        self.search_entry = ttk.Entry(controls, width=24)
        self.search_entry.pack(side="left", padx=4)
        ttk.Button(controls, text="Search", command=self.search_event).pack(side="left", padx=4)

        event_frame = ttk.LabelFrame(self.root, text="Events", padding=8)
        event_frame.pack(fill="both", expand=True, padx=14, pady=6)
        columns = ("id", "name", "date", "participants")
        self.event_tree = ttk.Treeview(event_frame, columns=columns, show="headings", height=8)
        for col, label, width in [
            ("id", "Event ID", 80), ("name", "Event Name", 300),
            ("date", "Event Date", 180), ("participants", "Participants", 140)
        ]:
            self.event_tree.heading(col, text=label)
            self.event_tree.column(col, width=width, anchor="center")
        self.event_tree.pack(fill="both", expand=True)

        venue_frame = ttk.LabelFrame(self.root, text="Venues", padding=8)
        venue_frame.pack(fill="both", expand=True, padx=14, pady=6)
        vcols = ("id", "name", "capacity", "status")
        self.venue_tree = ttk.Treeview(venue_frame, columns=vcols, show="headings", height=5)
        for col, label, width in [
            ("id", "Venue ID", 80), ("name", "Venue Name", 300),
            ("capacity", "Capacity", 150), ("status", "Availability", 150)
        ]:
            self.venue_tree.heading(col, text=label)
            self.venue_tree.column(col, width=width, anchor="center")
        self.venue_tree.pack(fill="both", expand=True)

        bottom = ttk.Frame(self.root, padding=10)
        bottom.pack(fill="x")
        ttk.Button(bottom, text="Allocate Venue to Selected Event", command=self.allocate_selected).pack(side="left")
        ttk.Button(bottom, text="Reset Venue Availability", command=self.reset_venues).pack(side="left", padx=8)
        self.status = ttk.Label(bottom, text="Ready")
        self.status.pack(side="right")

    def refresh_events(self, events=None):
        for item in self.event_tree.get_children():
            self.event_tree.delete(item)
        for event in (EVENTS if events is None else events):
            self.event_tree.insert("", "end", values=(
                event["id"], event["name"], event["date"], event["participants"]
            ))

    def refresh_venues(self):
        for item in self.venue_tree.get_children():
            self.venue_tree.delete(item)
        for venue in VENUES:
            status = "Available" if venue["available"] else "Booked"
            self.venue_tree.insert("", "end", values=(
                venue["id"], venue["name"], venue["capacity"], status
            ))

    def sort_events(self):
        self.refresh_events(merge_sort(EVENTS, "date"))
        self.status.config(text="Events sorted by date using Merge Sort")

    def search_event(self):
        name = self.search_entry.get().strip()
        if not name:
            messagebox.showinfo("Search", "Enter an event name.")
            return
        result = binary_search_event(EVENTS, name)
        if result:
            self.refresh_events([result])
            self.status.config(text="Event found using Binary Search")
        else:
            self.refresh_events([])
            self.status.config(text="No matching event found")
            messagebox.showinfo("Search", "Event not found.")

    def allocate_selected(self):
        selected = self.event_tree.selection()
        if not selected:
            messagebox.showinfo("Venue Allocation", "Select an event first.")
            return
        values = self.event_tree.item(selected[0], "values")
        event_id = int(values[0])
        event = next((item for item in EVENTS if item["id"] == event_id), None)
        venue = greedy_allocate_venue(event["participants"])
        if venue is None:
            messagebox.showwarning("Venue Allocation", "No available venue has sufficient capacity.")
            return
        venue["available"] = False
        booking_id = len(BOOKINGS) + 1
        BOOKINGS.append({
            "booking_id": booking_id, "event_id": event_id, "venue_id": venue["id"]
        })
        self.refresh_venues()
        messagebox.showinfo(
            "Booking Successful",
            f'{event["name"]} allocated to {venue["name"]}.\n'
            f'Capacity: {venue["capacity"]}\nBooking ID: {booking_id}'
        )
        self.status.config(text=f'{venue["name"]} allocated to {event["name"]}')

    def reset_venues(self):
        for venue in VENUES:
            venue["available"] = True
        BOOKINGS.clear()
        self.refresh_venues()
        self.status.config(text="Demo data reset")


if __name__ == "__main__":
    root = tk.Tk()
    app = CampusEventApp(root)
    root.mainloop()
