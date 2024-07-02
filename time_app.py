##   built_by_Beck
##   This is a simple time conversion app that I wrote to help me at my last job. It 2 inputs (start and end time) and returns a total number of minutes worked from those two times.
##   **Time must be entered in 24hr format **ex. 0735 would be 7:35 am   or  1420 would be 2:20 pm  




import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_time():
    start_time = start_entry.get()
    end_time = end_entry.get()

    try:
        # Convert input times to datetime objects
        start_time_dt = datetime.strptime(start_time, "%H%M")
        end_time_dt = datetime.strptime(end_time, "%H%M")

        # Calculate time difference
        time_difference = end_time_dt - start_time_dt

        # Calculate total minutes worked
        total_minutes = time_difference.total_seconds() / 60

        result_label.config(text=f"Total time worked was {int(total_minutes)} minutes.")
    except ValueError:
        messagebox.showerror("Error", "Please enter the time in 24-hour format (HHMM), e.g., 0900 for 9 AM.")
        result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Work Time Calculator")

# Adjust the initial size of the window
root.geometry("400x200")  # You can adjust the size as needed

# Add "Built_by_Beck" label under the title
built_by_label = tk.Label(root, text="Built_by_Beck", font=('Helvetica', 10, 'italic'))
built_by_label.pack()

# Start time entry
start_label = tk.Label(root, text="Enter start time (HHMM):")
start_label.pack()

start_entry = tk.Entry(root)
start_entry.pack()

# End time entry
end_label = tk.Label(root, text="Enter end time (HHMM):")
end_label.pack()

end_entry = tk.Entry(root)
end_entry.pack()

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_time)
calculate_button.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
