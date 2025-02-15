import tkinter as tk
from tkinter import messagebox

class Workout:
    def __init__(self, date, exercise_type, duration, calories_burned):
        self.date = date
        self.exercise_type = exercise_type
        self.duration = duration
        self.calories_burned = calories_burned

    def __str__(self):
        return f"{self.date}: {self.exercise_type} for {self.duration} minutes, {self.calories_burned} calories burned"

class User:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)

    def view_workouts(self):
        for workout in self.workouts:
            print(workout)

    def save_data(self, filename):
        with open(filename, 'w') as file:
            for workout in self.workouts:
                file.write(f"{workout.date},{workout.exercise_type},{workout.duration},{workout.calories_burned}\n")

    def load_data(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                date, exercise_type, duration, calories_burned = line.strip().split(',')
                workout = Workout(date, exercise_type, int(duration), int(calories_burned))
                self.workouts.append(workout)

def add_workout_ui(user):
    def save_workout():
        date = date_entry.get()
        exercise_type = exercise_type_entry.get()
        duration = int(duration_entry.get())
        calories_burned = int(calories_burned_entry.get())
        workout = Workout(date, exercise_type, duration, calories_burned)
        user.add_workout(workout)
        messagebox.showinfo("Success", "Workout added successfully!")

    add_workout_window = tk.Toplevel()
    add_workout_window.title("Add Workout")
    add_workout_window.configure(bg='black')

    tk.Label(add_workout_window, text="Date (YYYY-MM-DD):", fg="white", bg="black", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10)
    date_entry = tk.Entry(add_workout_window, font=("Arial", 14), bg="gray20", fg="white", insertbackground="white")
    date_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(add_workout_window, text="Exercise Type:", fg="white", bg="black", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=10)
    exercise_type_entry = tk.Entry(add_workout_window, font=("Arial", 14), bg="gray20", fg="white", insertbackground="white")
    exercise_type_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(add_workout_window, text="Duration (minutes):", fg="white", bg="black", font=("Arial", 14)).grid(row=2, column=0, padx=10, pady=10)
    duration_entry = tk.Entry(add_workout_window, font=("Arial", 14), bg="gray20", fg="white", insertbackground="white")
    duration_entry.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(add_workout_window, text="Calories Burned:", fg="white", bg="black", font=("Arial", 14)).grid(row=3, column=0, padx=10, pady=10)
    calories_burned_entry = tk.Entry(add_workout_window, font=("Arial", 14), bg="gray20", fg="white", insertbackground="white")
    calories_burned_entry.grid(row=3, column=1, padx=10, pady=10)

    add_button = tk.Button(add_workout_window, text="Add Workout", font=("Arial", 14), bg="green", fg="black", command=save_workout)
    add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=20)

def view_workouts_ui(user):
    view_workouts_window = tk.Toplevel()
    view_workouts_window.title("View Workouts")
    view_workouts_window.configure(bg='black')

    text = tk.Text(view_workouts_window, font=("Arial", 14), bg="gray20", fg="white", insertbackground="white")
    text.pack(padx=10, pady=10)

    workouts_info = "\n".join(str(workout) for workout in user.workouts)
    text.insert(tk.END, workouts_info)

def main():
    def save_data():
        filename = filename_entry.get()
        user.save_data(filename)
        messagebox.showinfo("Success", "Data saved successfully!")

    def load_data():
        filename = filename_entry.get()
        user.load_data(filename)
        messagebox.showinfo("Success", "Data loaded successfully!")

    def create_user():
        name = name_entry.get()
        age = int(age_entry.get())
        weight = float(weight_entry.get())
        global user
        user = User(name, age, weight)
        user_info_window.destroy()
        main_window.deiconify()

    main_window = tk.Tk()
    main_window.title("Workout Tracker")
    main_window.configure(bg='black')
    main_window.withdraw()  # Hide the main window initially

    user_info_window = tk.Toplevel()
    user_info_window.title("User Information")
    user_info_window.configure(bg='black')

    tk.Label(user_info_window, text="Enter your information", fg="white", bg="black", font=("Arial", 18)).pack(pady=20)

    tk.Label(user_info_window, text="Name:", fg="white", bg="black", font=("Arial", 14)).pack(pady=5)
    name_entry = tk.Entry(user_info_window, font=("Arial", 14), bg="gray20", fg="white", insertbackground="white")
    name_entry.pack(pady=5)

    tk.Label(user_info_window, text="Age:", fg="white", bg="black", font=("Arial", 14)).pack(pady=5)
    age_entry = tk.Entry(user_info_window, font=("Arial", 14), bg="gray20", fg="white", insertbackground="white")
    age_entry.pack(pady=5)

    tk.Label(user_info_window, text="Weight:", fg="white", bg="black", font=("Arial", 14)).pack(pady=5)
    weight_entry = tk.Entry(user_info_window, font=("Arial", 14), bg="gray20", fg="white", insertbackground="white")
    weight_entry.pack(pady=5)

    submit_button = tk.Button(user_info_window, text="Submit", font=("Arial", 14), bg="blue", fg="white", command=create_user)
    submit_button.pack(pady=20)

    tk.Label(main_window, text="Workout Tracker", fg="white", bg="black", font=("Arial", 24)).pack(pady=20)

    add_button = tk.Button(main_window, text="Add Workout", font=("Arial", 14), bg="blue", fg="white", command=lambda: add_workout_ui(user))
    add_button.pack(pady=10)

    view_button = tk.Button(main_window, text="View Workouts", font=("Arial", 14), bg="blue", fg="white", command=lambda: view_workouts_ui(user))
    view_button.pack(pady=10)

    tk.Label(main_window, text="Filename:", fg="white", bg="black", font=("Arial", 14)).pack(pady=10)
    filename_entry = tk.Entry(main_window, font=("Arial", 14), bg="gray20", fg="white", insertbackground="white")
    filename_entry.pack(pady=10)

    save_button = tk.Button(main_window, text="Save Data", font=("Arial", 14), bg="blue", fg="white", command=save_data)
    save_button.pack(pady=10)

    load_button = tk.Button(main_window, text="Load Data", font=("Arial", 14), bg="blue", fg="white", command=load_data)
    load_button.pack(pady=10)

    main_window.mainloop()

if __name__ == "__main__":
    main()
