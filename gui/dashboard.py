import tkinter as tk
from recommender.workout_engine import WorkoutRecommender

engine = WorkoutRecommender("aerobico", 170, 18)

def run_gui():
    root = tk.Tk()
    root.title("Smartband Feedback")

    hr_var = tk.StringVar()
    feedback_var = tk.StringVar()

    def on_submit():
        hr = int(hr_var.get())
        feedback = engine.suggest(hr)
        feedback_var.set(feedback)

    tk.Entry(root, textvariable=hr_var).pack()
    tk.Button(root, text="Enviar", command=on_submit).pack()
    tk.Label(root, textvariable=feedback_var).pack()

    root.mainloop()
