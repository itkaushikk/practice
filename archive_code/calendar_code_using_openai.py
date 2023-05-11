import tkinter as tk
import datetime

class CalendarApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calendar App")
        self.current_date = datetime.date.today()
        self.create_widgets()

    def create_widgets(self):
        # Create calendar widget
        self.calendar = tk.Calendar(self.master, selectmode='day', year=self.current_date.year, month=self.current_date.month, day=self.current_date.day)
        self.calendar.pack()

        # Create navigation buttons
        self.prev_button = tk.Button(self.master, text="Prev", command=self.prev_month)
        self.prev_button.pack(side='left')
        self.next_button = tk.Button(self.master, text="Next", command=self.next_month)
        self.next_button.pack(side='right')

        # Create event entry widget
        self.event_entry = tk.Entry(self.master)
        self.event_entry.pack()
        self.add_event_button = tk.Button(self.master, text="Add Event", command=self.add_event)
        self.add_event_button.pack()

    def prev_month(self):
        # Update calendar widget to display previous month
        self.current_date = self.current_date.replace(day=1) - datetime.timedelta(days=1)
        self.calendar.config(year=self.current_date.year, month=self.current_date.month)

    def next_month(self):
        # Update calendar widget to display next month
        self.current_date = self.current_date.replace(day=28) + datetime.timedelta(days=4)
        self.calendar.config(year=self.current_date.year, month=self.current_date.month)

    def add_event(self):
        # Get selected date and event details
        date = self.calendar.selection_get()
        event = self.event_entry.get()

        # TODO: Save event to file or database

        # Clear event entry widget
        self.event_entry.delete(0, 'end')

root = tk.Tk()
app = CalendarApp(root)
root.mainloop()